# config.py
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")

SCOPE = (
    "user-read-private "
    "user-read-email "
    "user-top-read "
    "user-library-read "
    "user-read-recently-played "
    "playlist-read-private "
    "playlist-modify-private "
    "playlist-modify-public"
)