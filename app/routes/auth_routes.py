from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Depends

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