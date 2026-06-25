import random
from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Depends
from app.database.supabase_client import supabase
from app.schemas.auth_schema import (
    ForgotPasswordSchema,
    ResetPasswordSchema
)

from app.utils.password_reset import (
    create_reset_token,
    verify_reset_token
)

from app.utils.email import send_reset_email

from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

from app.schemas.auth_schema import (
    RegisterSchema,
    LoginSchema
)

from app.services.auth_service import (
    register_user,
    login_user
)

from app.core.dependencies import (
    get_current_user
)

router = APIRouter()


@router.post("/register")
def register(user: RegisterSchema):

    created_user = register_user(user)

    if created_user is None:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    return {
        "message": "User created successfully"
    }


@router.post("/login")
def login(data: LoginSchema):

    response = login_user(data)

    if response is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    return response


@router.get("/profile")
def profile(
        current_user=Depends(
            get_current_user
        )
):

    return current_user

@router.post("/forgot-password")
async def forgot_password(
    body: ForgotPasswordSchema
):
    user = (
        supabase.table("users")
        .select("*")
        .eq("email", body.email)
        .execute()
    )

    if not user.data:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    code = str(
        random.randint(100000, 999999)
    )

    supabase.table("users").update({
        "reset_code": code
    }).eq(
        "email",
        body.email
    ).execute()

    await send_reset_email(
        body.email,
        code
    )

    return {
        "message": "Reset code sent"
    }

@router.post("/reset-password")
async def reset_password(
    body: ResetPasswordSchema
):
    user = (
        supabase.table("users")
        .select("*")
        .eq("email", body.email)
        .eq("reset_code", body.code)
        .execute()
    )

    if not user.data:
        raise HTTPException(
            status_code=400,
            detail="Invalid reset code"
        )

    hashed_password = pwd_context.hash(
        body.new_password
    )

    supabase.table("users").update({
        "password": hashed_password,
        "reset_code": None
    }).eq(
        "email",
        body.email
    ).execute()

    return {
        "message":
        "Password updated successfully"
    }
