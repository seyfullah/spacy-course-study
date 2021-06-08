import spacy

from spacy.lang.tr import Turkish
nlp = Turkish()
doc = nlp("Berlin güzel bir şehir gibi görünüyor")

# Iterate over the tokens
for token in doc:
    # Check if the current token is a proper noun
    if token.pos_ == "PROPN":
        # Check if the next token is a verb
        if doc[token.i + 1].pos_ == "VERB":
            print("Fiilden önce uygun bir isim bulundu:", token.text)