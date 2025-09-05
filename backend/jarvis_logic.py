from training.speech_text_transform import speech_to_text, text_to_speech
import datetime
import webbrowser
import os
import sys
import joblib
import warnings
from sklearn.exceptions import InconsistentVersionWarning

warnings.filterwarnings("ignore", category=InconsistentVersionWarning)

# Load trained intent classifier
clf = joblib.load("intent_classifier.pkl")

# Define intent constants
get_time = 0
search_google = 1
search_youtube = 2
open_notepad = 3
open_calculator = 4
open_whatsapp = 5
open_linkedin = 6
open_github = 7
open_spotify = 8
exit = 9

def execute_intent(intent):
    if intent == get_time:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        text_to_speech(f"The current time is {current_time}")
        return f"Current Time: {current_time}"

    elif intent == search_google:
        text_to_speech("What do you want to search on Google?")
        query = speech_to_text()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            text_to_speech(f"Searching Google for {query}")
            return f"Searching Google for {query}"

    elif intent == search_youtube:
        text_to_speech("What do you want to search on YouTube?")
        query = speech_to_text()
        if query:
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
            text_to_speech(f"Searching YouTube for {query}")
            return f"Searching YouTube for {query}"

    elif intent == open_notepad:
        os.system("notepad.exe")
        text_to_speech("Opening Notepad")
        return "Opened Notepad"

    elif intent == open_calculator:
        os.system("calc.exe")
        text_to_speech("Opening Calculator")
        return "Opened Calculator"

    elif intent == open_whatsapp:
        webbrowser.open("https://web.whatsapp.com/")
        text_to_speech("Opening WhatsApp")
        return "Opened WhatsApp"

    elif intent == open_linkedin:
        webbrowser.open("https://www.linkedin.com/")
        text_to_speech("Opening LinkedIn")
        return "Opened LinkedIn"

    elif intent == open_github:
        webbrowser.open("https://github.com/")
        text_to_speech("Opening GitHub")
        return "Opened GitHub"

    elif intent == open_spotify:
        os.system("spotify.exe")
        text_to_speech("Opening Spotify")
        return "Opened Spotify"

    elif intent == exit:
        text_to_speech("Goodbye! Shutting down.")
        sys.exit()

    else:
        text_to_speech("Sorry, I don't know how to handle this intent yet.")
        return "Unknown Intent"

def find_intent(command):
    return clf.predict([command])[0]

def activate_jarvis():
    text_to_speech("Jarvis Activated!")
    return "Jarvis Activated! Listening..."
