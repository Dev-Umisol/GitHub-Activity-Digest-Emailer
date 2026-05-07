from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from .database import Base

# This table will store user information, including their GitHub ID, username, and email
class Users(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    github_id = Column(Integer, nullable=False, unique=True)
    user_name = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)

# This table will store the GitHub OAuth tokens for each user, allowing us to access the GitHub API on their behalf
class GithubTokens(Base):
    __tablename__ = "github_tokens"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    access_token = Column(String, nullable=False)
    refresh_token = Column(String, nullable=True)
    expires_at = Column(DateTime, nullable=False)

# This table will store the repositories that users are watching for updates
class WatchedRepos(Base):
    __tablename__ = "watched_repos"
    
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    repo_name = Column(String, primary_key=True)

# This table will store user preferences for notifications, such as frequency and last run time
class UserPreferences(Base):
    __tablename__ = "user_preferences"
    
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    frequency = Column(String, nullable=False, default="daily")  # e.g., "daily", "weekly"
    last_run_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)