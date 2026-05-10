from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from urllib.parse import urlencode
from dotenv import load_dotenv

import secrets
import os

# Key configuration
load_dotenv()
GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")
SECRET_KEY = os.getenv("SECRET_KEY")

if GITHUB_CLIENT_ID is None or GITHUB_CLIENT_SECRET is None:
    raise ValueError("GITHUB_CLIENT_ID or GITHUB_CLIENT_SECRET must be set in the environment variables.")

if SECRET_KEY is None:
    raise ValueError("SECRET_KEY must be set in the environment variables.")

router = APIRouter()

#TODO FIX
@router.get("/auth/redirect")
async def auth_redirect(request: Request):
    # Generate a random state parameter for CSRF protection
    state = secrets.token_urlsafe(16)

    # Store the state in the session (or database) for later verification
    request.session["oauth_state"] = state

    # Build the GitHub authorization URL
    params = {
        "client_id": GITHUB_CLIENT_ID,
        "redirect_uri": request.url_for("auth_callback"),
        "scope": "read:user user:email",
        "state": state
    }
    github_auth_url = f"https://github.com/login/oauth/authorize?{urlencode(params)}"