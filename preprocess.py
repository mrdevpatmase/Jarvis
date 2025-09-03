import spacy



nlp = spacy.load("en_core_web_sm")
doc = nlp("Hello Jarvis! Can you open the Chrome browser?")
tokens = [token.lemma_.lower() for token in doc if not token.is_stop and token.is_alpha]
print(tokens)
