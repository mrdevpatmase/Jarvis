import joblib
import webbrowser
import os
from datetime import datetime
import speech_recognition as sr
import pyaudio
import pyttsx3

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)        
        querry =r.recognize_google(audio)
        print(querry) 
        return querry

def text_to_speech(info):
    engine = pyttsx3.init()
    engine.say(info)
    engine.runAndWait()

# Define actions for each intent
def execute_intent(intent):
    if intent == "get_time":
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Current Time:", current_time)
        text_to_speech(f"The current time is {current_time}")

    elif intent == "search_google":
        text_to_speech("What do you want to search on Google?")
        query = speech_to_text()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            text_to_speech(f"Searching Google for {query}")

    elif intent == "search_youtube":
        text_to_speech("What do you want to search on YouTube?")
        query = speech_to_text()
        if query:
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
            text_to_speech(f"Searching YouTube for {query}")

    elif intent == "open_notepad":
        os.system("notepad.exe")
        text_to_speech("Opening Notepad")

    elif intent == "open_calculator":
        os.system("calc.exe")
        text_to_speech("Opening Calculator")

    elif intent == "open_whatsapp":
        webbrowser.open("https://web.whatsapp.com/")
        text_to_speech("Opening WhatsApp")

    elif intent == "open_linkedin":
        webbrowser.open("https://www.linkedin.com/")
        text_to_speech("Opening LinkedIn")

    elif intent == "open_github":
        webbrowser.open("https://github.com/")
        text_to_speech("Opening GitHub")

    elif intent == "open_spotify":
        webbrowser.open("https://open.spotify.com/")
        text_to_speech("Opening Spotify")

    else:
        text_to_speech("Sorry, I don't know how to handle this intent yet.")


# Load the trained model (saved pipeline)
clf = joblib.load("intent_classifier.pkl")

# Main loop
if __name__ == "__main__":
    print("🤖 Jarvis AI is ready! Say 'quit' or 'exit' to stop.\n")

    while True:
        # Take voice command
        command = speech_to_text()
        if not command:
            continue

        print(f"🎙️ You said: {command}")

        if command.lower() in ["quit", "exit", "bye"]:
            text_to_speech("Goodbye! Have a nice day.")
            print("👋 Goodbye!")
            break

        # Predict intent
        intent = clf.predict([command])[0]
        print(f"📌 Predicted Intent: {intent}")

        # Execute corresponding action
        execute_intent(intent)
