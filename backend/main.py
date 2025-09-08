from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from pathlib import Path
import joblib
import datetime
import os

# -------- Paths ----------
HERE = Path(__file__).resolve()
BACKEND_DIR = HERE.parent
PROJECT_ROOT = BACKEND_DIR.parent
FRONTEND_DIR = PROJECT_ROOT / "frontend"

# -------- App ----------
app = FastAPI(title="Jarvis v1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten later to your domain(s)
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve the entire frontend folder; / will return index.html
app.mount("/", StaticFiles(directory=str(FRONTEND_DIR), html=True), name="frontend")

# -------- Model ----------
# Pin scikit-learn version in requirements to match your training env.
MODEL_PATH = BACKEND_DIR / "intent_classifier.pkl"
clf = joblib.load(str(MODEL_PATH))

# Intent IDs (must match your training)
GET_TIME = 0
SEARCH_GOOGLE = 1
SEARCH_YOUTUBE = 2
OPEN_NOTEPAD = 3
OPEN_CALC = 4
OPEN_WHATSAPP = 5
OPEN_LINKEDIN = 6
OPEN_GITHUB = 7
OPEN_SPOTIFY = 8
EXIT_INTENT = 9

class Command(BaseModel):
    command: str

def plan_action(intent: int, command_text: str):
    """
    Cloud-safe: instead of trying to open apps on the server,
    return instructions for the *browser* (frontend) to execute.
    """
    if intent == GET_TIME:
        return {"type": "say", "text": f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}"}

    if intent == SEARCH_GOOGLE:
        return {"type": "open_url", "url": f"https://www.google.com/search?q={command_text}"}

    if intent == SEARCH_YOUTUBE:
        return {"type": "open_url", "url": f"https://www.youtube.com/results?search_query={command_text}"}

    # The following are desktop-only. In the cloud, just tell the user.
    if intent in [OPEN_NOTEPAD, OPEN_CALC, OPEN_SPOTIFY]:
        return {"type": "say", "text": "That action needs your desktop. I can’t open local apps from the cloud."}

    if intent == OPEN_WHATSAPP:
        return {"type": "open_url", "url": "https://web.whatsapp.com/"}

    if intent == OPEN_LINKEDIN:
        return {"type": "open_url", "url": "https://www.linkedin.com/"}

    if intent == OPEN_GITHUB:
        return {"type": "open_url", "url": "https://github.com/"}

    if intent == EXIT_INTENT:
        return {"type": "say", "text": "Jarvis online services don’t support exit."}

    return {"type": "say", "text": "Sorry, I don't know how to handle this command."}

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/process_command")
def process_command(cmd: Command):
    try:
        intent = int(clf.predict([cmd.command])[0])
    except Exception as e:
        return JSONResponse({"error": f"intent prediction failed: {e}"}, status_code=500)
    action = plan_action(intent, cmd.command)
    return JSONResponse({"action": action})
