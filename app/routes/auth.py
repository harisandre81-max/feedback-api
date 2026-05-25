# routes/auth.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.security import hash_password, verify_password
from app.core.jwt import create_token
from app.database.deps import get_db
from app.models.user import User
from app.core.security import hash_password
from app.schemas.auth import RegisterSchema, LoginSchema

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
def register(data: RegisterSchema, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.email == data.email).first()

    if user:
        raise HTTPException(400, "User already exists")

    new_user = User(
        name=data.name,
        email=data.email,
        password=hash_password(data.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created"}

@router.post("/login")
def login(data: LoginSchema, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.email == data.email).first()

    if not user or not verify_password(data.password, user.password):
        raise HTTPException(401, "Invalid credentials")

    token = create_token({"user_id": user.id})

    return {
        "access_token": token,
        "token_type": "bearer"
    }