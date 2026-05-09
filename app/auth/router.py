from fastapi.responses import RedirectResponse
from urllib.parse import urlencode
from dotenv import load_dotenv

import os

# Key configuration
load_dotenv()
GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")