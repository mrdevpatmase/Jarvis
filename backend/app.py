from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import joblib
import os
import datetime
import webbrowser
import sys
from pydantic import BaseModel

# ------------------- Setup -------------------
app = FastAPI()

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")
BACKEND_DIR = os.path.dirname(os.path.abspath(__file__))

# Load classifier
clf = joblib.load(os.path.join(BACKEND_DIR, "intent_classifier.pkl"))

# Mount frontend static files
app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

# Model for incoming command
class Command(BaseModel):
    command: str

# Serve frontend
@app.get("/", response_class=HTMLResponse)
async def serve_home():
    index_file = os.path.join(FRONTEND_DIR, "index.html")
    with open(index_file, "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())

# ------------------- Define intents -------------------
get_time = 0
search_google = 1
search_youtube = 2
open_notepad = 3
open_calculator = 4
open_whatsapp = 5
open_linkedin = 6
open_github = 7
open_spotify = 8
exit_intent = 9

def execute_intent(intent, command_text):
    if intent == get_time:
        return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}"
    elif intent == search_google:
        webbrowser.open(f"https://www.google.com/search?q={command_text}")
        return f"Searching Google for {command_text}"
    elif intent == search_youtube:
        webbrowser.open(f"https://www.youtube.com/results?search_query={command_text}")
        return f"Searching YouTube for {command_text}"
    elif intent == open_notepad:
        os.system("notepad.exe")
        return "Opening Notepad"
    elif intent == open_calculator:
        os.system("calc.exe")
        return "Opening Calculator"
    elif intent == open_whatsapp:
        webbrowser.open("https://web.whatsapp.com/")
        return "Opening WhatsApp"
    elif intent == open_linkedin:
        webbrowser.open("https://www.linkedin.com/")
        return "Opening LinkedIn"
    elif intent == open_github:
        webbrowser.open("https://github.com/")
        return "Opening GitHub"
    elif intent == open_spotify:
        os.system("spotify.exe")
        return "Opening Spotify"
    elif intent == exit_intent:
        sys.exit()
    else:
        return "Sorry, I don't know how to handle this command."

# ------------------- Command endpoint -------------------
@app.post("/process_command")
async def process_command(cmd: Command):
    intent = clf.predict([cmd.command])[0]
    response_text = execute_intent(intent, cmd.command)
    return JSONResponse({"response": response_text})
