import spacy
from speech_text_transform import speech_to_text, text_to_speech

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Use speech_to_text to capture voice input
text = speech_to_text() 
text_to_speech(f"You said: {text}") 

# Preprocess text with spaCy
doc = nlp(text)
tokens = [token.lemma_.lower() for token in doc if not token.is_stop and token.is_alpha]

print("Processed tokens:", tokens)
