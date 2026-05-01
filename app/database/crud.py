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

# UserPreferences CRUD Operations
# This function creates a new preferences entry for a user, which can be used to store their notification settings
def create_preferences(db: Session, user_id: int):
    pass

# This function retrieves a user's preferences, which can be used to determine how often they want to receive notifications
def get_preferences(db: Session, user_id: int):
    pass

# This function updates a user's preferences, allowing them to change their notification settings
def update_preferences(db: Session, user_id: int, frequency: str):
    pass

# This function updates the last run time for a user's preferences, which can be used to determine when to send the next notification
def update_last_run_at(db: Session, user_id: int, last_run_at):
    pass

# WatchedRepos CRUD Operations
# This function adds a repository to a user's watch list, allowing them to receive notifications about updates to that repository
def add_repo(db: Session, user_id: int, repo_name: str):
    pass

# This function retrieves a specific repository from a user's watch list, which can be used to check if they are watching that repository
def get_repo(db: Session, user_id: int, repo_name: str):
    pass

# This function deletes a repository from a user's watch list, which can be used to stop notifications about updates to that repository
def delete_repo(db: Session, user_id: int, repo_name: str):
    pass

# GithubTokens CRUD Operations
# This function creates a new token entry for a user, which can be used to store their GitHub OAuth tokens for accessing the GitHub API
def create_token(db: Session, user_id: int, access_token: str, refresh_token: str, expires_at):
    pass

# This function retrieves a user's token, which can be used to access the GitHub API on their behalf
def retrieve_token(db: Session, user_id: int):
    pass

# This function updates a user's token, allowing us to refresh their GitHub OAuth tokens when they expire
def update_token(db: Session, user_id: int, access_token: str, refresh_token: str, expires_at):
    pass
