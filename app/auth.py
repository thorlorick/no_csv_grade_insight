from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from google_auth_oauthlib.flow import Flow

router = APIRouter()

# Load secret file from Render's mounted secret
client_secrets_file = "/etc/secrets/GOOGLE_OAUTH_CLIENT_JSON"

# This must match what you put in Google Cloud
REDIRECT_URI = "https://no-csv-grade-insight.onrender.com/auth/callback"

SCOPES = ["https://www.googleapis.com/auth/classroom.courses.readonly"]

@router.get("/login")
def login():
    flow = Flow.from_client_secrets_file(
        client_secrets_file=client_secrets_file,
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI
    )
    auth_url, _ = flow.authorization_url(prompt='consent')
    return RedirectResponse(auth_url)

@router.get("/auth/callback")
def callback(request: Request):
    return {"message": "OAuth callback received!"}

