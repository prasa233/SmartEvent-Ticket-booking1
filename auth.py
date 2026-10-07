
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User
from app.schemas import RegisterRequest, LoginRequest
from app.auth import (
    hash_password,
    verify_password,
    create_access_token,
)


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


# ==================================================
# REGISTER
# ==================================================

@router.post("/register")
def register(
    user_data: RegisterRequest,
    db: Session = Depends(get_db),
):
    # Check email
    existing_email = (
        db.query(User)
        .filter(User.email == user_data.email)
        .first()
    )

    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="Email already registered",
        )

    # Check username
    existing_username = (
        db.query(User)
        .filter(User.username == user_data.username)
        .first()
    )

    if existing_username:
        raise HTTPException(
            status_code=400,
            detail="Username already exists",
        )

    # Hash password
    hashed_password = hash_password(
        user_data.password
    )

    # Create user
    new_user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hashed_password,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "user_id": new_user.id,
        "username": new_user.username,
        "email": new_user.email,
    }


# ==================================================
# LOGIN
# ==================================================

@router.post("/login")
def login(
    login_data: LoginRequest,
    db: Session = Depends(get_db),
):
    # Find user by email
    user = (
        db.query(User)
        .filter(User.email == login_data.email)
        .first()
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    # Verify password
    if not verify_password(
        login_data.password,
        user.hashed_password,
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    # Create JWT
    token = create_access_token({
        "sub": str(user.id)
    })

    return {
        "access_token": token,
        "token_type": "bearer",
    }

