from fastapi import APIRouter, Path, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from users.schemas import (
    UserLoginSchema, UserRegisterSchema, 
)
from users.models import UserModel
from sqlalchemy.orm import Session
from core.database import get_db
from typing import List


router = APIRouter()

@router.post("/login")
async def user_login(
        user_info: UserLoginSchema,
        db: Session = Depends(get_db),
    ):
    fetched_user = db.query(UserModel).where(UserModel.username==user_info.username).first()
    if not fetched_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"username: '{user_info.username}' doesn't exists. Register first.")
    if not fetched_user.verify_password(user_info.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Invalid password, try again.")
        
    return {"detail": f"Welcome {fetched_user.username}"}

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def user_register(
    user_info: UserRegisterSchema,
    db: Session = Depends(get_db),
):
    query = db.query(UserModel).where(UserModel.username==user_info.username).first()
    if query:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"username: {user_info.username} already exists. Try Login instead of register")
    
    user_data = user_info.model_dump()
    user_data.pop("password_confirm", None)
    
    new_user = UserModel(**user_data)
    new_user.set_password(user_info.password)
    
    db.add(new_user)
    db.commit()
    
    response_content={"detail": f"User {new_user.username} registered successfully."}
    
    return JSONResponse(
        content=response_content    
    )
    
@router.delete("/register", status_code=status.HTTP_201_CREATED)
async def user_register(
    user_id: int,
    db: Session = Depends(get_db),
):
    query = db.query(UserModel).where(UserModel.id==user_id).first()
    if not query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"username: {user_id} not exists.")
    
    db.delete(query)
    db.commit()
    
    response_content={"detail": f"User {query.username} deleted successfully."}
    
    return JSONResponse(
        content=response_content    
    )