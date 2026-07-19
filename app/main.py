# main.py
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.spotify import *

app = FastAPI(title="Spotify AI Agent")

token = {}


@app.get("/")
def home():
    return {"message": "Spotify AI Agent"}


@app.get("/login")
def login():

    return RedirectResponse(get_auth_url())


@app.get("/callback")
def callback(code: str):

    global token

    token = get_token(code)

    return {
        "message": "Login Successful"
    }


@app.get("/profile")
def profile():

    sp = get_spotify_client(token["access_token"])

    return sp.current_user()


@app.get("/top-tracks")
def top_tracks():

    sp = get_spotify_client(token["access_token"])

    return sp.current_user_top_tracks(limit=10)


@app.get("/top-artists")
def top_artists():

    sp = get_spotify_client(token["access_token"])

    return sp.current_user_top_artists(limit=10)