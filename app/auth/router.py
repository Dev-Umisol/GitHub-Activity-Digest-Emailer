from fastapi.responses import RedirectResponse
from urllib.parse import urlencode
from dotenv import load_dotenv

import os

# Key configuration
load_dotenv()
GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")

if GITHUB_CLIENT_ID is None or GITHUB_CLIENT_SECRET is None:
    raise ValueError("GITHUB_CLIENT_ID or GITHUB_CLIENT_SECRET must be set in the environment variables.")