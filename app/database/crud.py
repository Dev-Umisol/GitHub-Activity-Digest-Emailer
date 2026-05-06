from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models

# CRUD operations for the database models
# This function retrieves a user by their GitHub ID, or creates a new user if one does not exist
def get_or_create_user(db: Session, github_id: int, user_name: str, email: str) -> models.Users:
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
def create_preferences(db: Session, user_id: int) -> models.UserPreferences | None:
    preferences = db.query(models.UserPreferences).filter(models.UserPreferences.user_id == user_id).first()
    
    if preferences:
        return preferences
    
    new_preferences = models.UserPreferences(user_id=user_id, frequency="daily")
    
    db.add(new_preferences)
    db.commit()
    db.refresh(new_preferences)
    
    return new_preferences

# This function retrieves a user's preferences, which can be used to determine how often they want to receive notifications
def get_preferences(db: Session, user_id: int) -> models.UserPreferences | None:
    return db.query(models.UserPreferences).filter(models.UserPreferences.user_id == user_id).first()

# This function updates a user's preferences, allowing them to change their notification settings
def update_preferences(db: Session, user_id: int, frequency: str) -> models.UserPreferences | None:
    preferences = db.query(models.UserPreferences).filter(models.UserPreferences.user_id == user_id).first()
    
    if not preferences:
        raise HTTPException(status_code=404, detail="User preferences not found")
    
    preferences.frequency = frequency # type: ignore
    
    db.commit()
    db.refresh(preferences)
    
    return preferences

# This function updates the last run time for a user's preferences, which can be used to determine when to send the next notification
def update_last_run_at(db: Session, user_id: int, last_run_at) -> models.UserPreferences | None:
    last_run = db.query(models.UserPreferences).filter(models.UserPreferences.user_id == user_id).first()
    
    if not last_run:
        raise HTTPException(status_code=404, detail="User preferences not found")
    
    last_run.last_run_at = last_run_at # type: ignore
        
    db.commit()
    db.refresh(last_run)
        
    return last_run

# WatchedRepos CRUD Operations
# This function adds a repository to a user's watch list, allowing them to receive notifications about updates to that repository
def add_repo(db: Session, user_id: int, repo_name: str) -> models.WatchedRepos | None:
    existing_repo = db.query(models.WatchedRepos).filter(models.WatchedRepos.user_id == user_id, models.WatchedRepos.repo_name == repo_name).first()
    
    if existing_repo:
        return existing_repo
    
    new_repo = models.WatchedRepos(user_id=user_id, repo_name=repo_name)
    
    db.add(new_repo)
    db.commit()
    db.refresh(new_repo)
    
    return new_repo
        

# This function retrieves a specific repository from a user's watch list, which can be used to check if they are watching that repository
def get_repo(db: Session, user_id: int, repo_name: str) -> models.WatchedRepos | None:
    return db.query(models.WatchedRepos).filter(models.WatchedRepos.user_id == user_id, models.WatchedRepos.repo_name == repo_name).first()

# This function deletes a repository from a user's watch list, which can be used to stop notifications about updates to that repository
def delete_repo(db: Session, user_id: int, repo_name: str) -> None:
    repo = db.query(models.WatchedRepos).filter(models.WatchedRepos.user_id == user_id, models.WatchedRepos.repo_name == repo_name).first()
    
    if not repo:
        raise HTTPException(status_code=404, detail="Repository not found in watch list")
    
    db.delete(repo)
    db.commit()

# GithubTokens CRUD Operations
# This function creates a new token entry for a user, which can be used to store their GitHub OAuth tokens for accessing the GitHub API

#TODO: FIX
def create_token(db: Session, user_id: int, access_token: str, refresh_token: str, expires_at) -> models.GithubTokens | None:
    token = db.query(models.GithubTokens).filter(models.GithubTokens.user_id == user_id).first()
    
    if token:
        return token
    
    new_token = models.GithubTokens(user_id=user_id, access_token=access_token, refresh_token=refresh_token, expires_at=expires_at)
    
    db.add(new_token)
    db.commit()
    db.refresh(new_token)
    
    return new_token

# This function retrieves a user's token, which can be used to access the GitHub API on their behalf
def retrieve_token(db: Session, user_id: int) -> models.GithubTokens | None:
    return db.query(models.GithubTokens).filter(models.GithubTokens.user_id == user_id).first()

# This function updates a user's token, allowing us to refresh their GitHub OAuth tokens when they expire
def update_token(db: Session, user_id: int, access_token: str, refresh_token: str, expires_at) -> models.GithubTokens | None:
    token = db.query(models.GithubTokens).filter(models.GithubTokens.user_id == user_id).first()
    
    if not token:
        raise HTTPException(status_code=404, detail="Token not found for user")
    
    token.access_token = access_token # type: ignore
    token.refresh_token = refresh_token # type: ignore
    token.expires_at = expires_at # type: ignore
    
    db.commit()
    db.refresh(token)
    
    return token
