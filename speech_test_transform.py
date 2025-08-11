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

def text_to_speech():
    engine = pyttsx3.init()
    engine.say("Hello, I am your Jarvis assistant.")
    engine.runAndWait()

# speech_to_text()
text_to_speech()