from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

router = APIRouter()

client_secrets_file = "/etc/secrets/GOOGLE_OAUTH_CLIENT_JSON"
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
async def callback(request: Request):
    flow = Flow.from_client_secrets_file(
        client_secrets_file=client_secrets_file,
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI
    )
    flow.fetch_token(authorization_response=str(request.url))

    credentials = flow.credentials

    user_service = build("oauth2", "v2", credentials=credentials)
    user_info = user_service.userinfo().get().execute()

    return {
        "access_token": credentials.token,
        "refresh_token": credentials.refresh_token,
        "expires_in": credentials.expiry.isoformat(),
        "email": user_info["email"],
        "name": user_info.get("name", "Unknown")
    }


