# spotify.py
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

from app.config import *


oauth = SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE
)


def get_auth_url():
    return oauth.get_authorize_url()


def get_token(code):
    return oauth.get_access_token(code)


def get_spotify_client(access_token):
    return Spotify(auth=access_token)