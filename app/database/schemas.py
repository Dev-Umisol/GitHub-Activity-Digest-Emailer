from pydantic import BaseModel, ConfigDict
from datetime import datetime

# Pydantic models for request and response validation
class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    github_id: int
    user_name: str
    email: str

# Model for user login request
class UserLogin(BaseModel):
    code: str

# Model for user preferences
class UserPreferences(BaseModel):
    frequency: str
    