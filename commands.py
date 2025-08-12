import webbrowser
from datetime import datetime
from speech_text_transform import speech_to_text, text_to_speech
import spacy
from spacy.matcher import PhraseMatcher

text_to_speech("Hi, I am Jarvis")

nlp = spacy.load("en_core_web_sm")
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")

# Define intents
intents = {
    "get_time": ["time please", "what's the time", "current time", "tell me the time"],
    "search_google": ["search google", "look up", "find on google", "google"],
    "search_youtube": ["play on youtube", "search youtube", "youtube video", "youtube"],
    "exit": ["quit", "exit", "close", "stop"]
}

# Add patterns to matcher
for intent, phrases in intents.items():
    patterns = [nlp(text) for text in phrases]
    matcher.add(intent, patterns)

while True:
    command = speech_to_text()
    if not command:
        continue
    
    doc = nlp(command.lower())
    matches = matcher(doc)

    if not matches:
        text_to_speech("Sorry, I didn't understand that.")
        continue

    intent_name = nlp.vocab.strings[matches[0][0]]  # Get matched intent name

    if intent_name == "get_time":
        time_now = datetime.now().strftime("%I:%M %p")
        print(time_now)
        text_to_speech(f"The time is {time_now}")

    elif intent_name == "search_google":
        search = command.lower().replace("google", "").strip()
        if search:
            webbrowser.open(f"https://www.google.com/search?q={search}")
            text_to_speech(f"Here are the results for {search}")
        else:
            text_to_speech("What should I search on Google?")

    elif intent_name == "search_youtube":
        search = command.lower().replace("youtube", "").strip()
        if search:
            webbrowser.open(f"https://www.youtube.com/results?search_query={search}")
            text_to_speech(f"Here are the results for {search}")
        else:
            text_to_speech("What should I search on YouTube?")

    elif intent_name == "exit":
        text_to_speech("Goodbye!")
        break
