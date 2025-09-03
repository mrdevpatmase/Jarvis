# in this file we define the intents for the jarvis

import csv

# Dataset: 12 commands per intent
dataset = {
    "get_time": [
        "What time is it?", "Can you tell me the time?", "Current time please",
        "Tell me the time", "What’s the current hour?", "Time now",
        "Could you give me the time?", "Do you know the time?", "Time check",
        "Show me the current time", "I want to know the time", "Give me the time now"
    ],
    "search_google": [
        "Search Google for Python tutorials", "Look up machine learning", "Find AI articles on Google",
        "Google best restaurants near me", "Search Google for Jarvis projects", "Find information about space on Google",
        "Look up weather today", "Google trending news", "Search for stock prices on Google",
        "Find nearby cafes", "Google news about technology", "Search Google for recipes"
    ],
    "search_youtube": [
        "Play music on YouTube", "Search YouTube for cat videos", "Find Python tutorials on YouTube",
        "Play cooking videos on YouTube", "Search YouTube for gaming videos", "Look up JavaScript tutorials on YouTube",
        "Play trending videos on YouTube", "Find motivational speeches on YouTube", "Search YouTube for workout videos",
        "Play piano tutorials on YouTube", "Look up movie trailers on YouTube", "Search YouTube for meditation videos"
    ],
    "open_notepad": [
        "Open Notepad", "Start Notepad", "Launch Notepad",
        "Open a new Notepad file", "I want to write something in Notepad", "Notepad please",
        "Can you open Notepad?", "Launch the Notepad app", "Start a Notepad session",
        "Open Notepad editor", "Notepad text editor", "Open Notepad program"
    ],
    "open_calculator": [
        "Open Calculator", "Launch Calculator", "Start Calculator",
        "I want to use Calculator", "Calculator please", "Can you open Calculator?",
        "Open the Calculator app", "Start a new Calculator session", "Calculator program",
        "Launch the Calculator tool", "Open my Calculator", "Use Calculator"
    ],
    "open_whatsapp": [
        "Open WhatsApp", "Launch WhatsApp", "Start WhatsApp",
        "I want to check WhatsApp", "Open WhatsApp messenger", "WhatsApp please",
        "Can you open WhatsApp?", "Start the WhatsApp app", "Launch WhatsApp program",
        "Open my WhatsApp", "Open WhatsApp chat", "Start WhatsApp messenger"
    ],
    "open_linkedin": [
        "Open LinkedIn", "Launch LinkedIn", "Start LinkedIn",
        "I want to check LinkedIn", "Open LinkedIn website", "LinkedIn please",
        "Can you open LinkedIn?", "Start the LinkedIn app", "Open my LinkedIn profile",
        "Launch LinkedIn program", "Check LinkedIn updates", "Open LinkedIn page"
    ],
    "open_github": [
        "Open GitHub", "Launch GitHub", "Start GitHub",
        "I want to check GitHub", "Open GitHub repository", "GitHub please",
        "Can you open GitHub?", "Start the GitHub app", "Open my GitHub profile",
        "Launch GitHub program", "Check GitHub updates", "Open GitHub page"
    ],
    "open_spotify": [
        "Open Spotify", "Launch Spotify", "Start Spotify",
        "I want to listen on Spotify", "Play music on Spotify", "Spotify please",
        "Can you open Spotify?", "Start the Spotify app", "Open my Spotify playlists",
        "Launch Spotify program", "Play songs on Spotify", "Open Spotify music"
    ]
}

# Write CSV
with open("jarvis_intents.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["command", "intent"])
    for intent, commands in dataset.items():
        for cmd in commands:
            writer.writerow([cmd, intent])

print("CSV 'jarvis_intents.csv' created with 108 commands.")
