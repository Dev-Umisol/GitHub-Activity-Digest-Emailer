from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models

# CRUD operations for the database models
# This function retrieves a user by their GitHub ID, or creates a new user if one does not exist
def get_or_create_user(db: Session, github_id: int, user_name: str, email: str):
    user = db.query(models.Users).filter(models.Users.github_id == github_id).first()
    
    if user:
        return user
    new_user = models.Users(github_id=github_id, user_name=user_name, email=email)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user