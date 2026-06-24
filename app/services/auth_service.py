from app.database.supabase_client import supabase

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)


def register_user(user):

    existing_user = (
        supabase
        .table("users")
        .select("*")
        .eq("email", user.email)
        .execute()
    )

    if existing_user.data:
        return None

    hashed_password = hash_password(
        user.password
    )

    result = (
        supabase
        .table("users")
        .insert({
            "full_name": user.full_name,
            "email": user.email,
            "password": hashed_password
        })
        .execute()
    )

    return result.data[0]


def login_user(data):

    user = (
        supabase
        .table("users")
        .select("*")
        .eq("email", data.email)
        .execute()
    )

    if not user.data:
        return None

    user = user.data[0]

    if not verify_password(
        data.password,
        user["password"]
    ):
        return None

    token = create_access_token(
        {
            "sub": user["id"],
            "email": user["email"]
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": user["id"],
            "full_name": user["full_name"],
            "email": user["email"]
        }
    }