import spacy

# Import the Matcher
from spacy.matcher import Matcher

# Load a model and create the nlp object
nlp = spacy.load("en_core_web_sm")

nlp.vocab.strings.add("coffee")
coffee_hash = nlp.vocab.strings["coffee"]
coffee_string = nlp.vocab.strings[coffee_hash]

string = nlp.vocab.strings[3197928453018144401]

doc = nlp("I love coffee")
print("hash value:", nlp.vocab.strings["coffee"])
print("string value:", nlp.vocab.strings[3197928453018144401])

print("hash value:", doc.vocab.strings["coffee"])

lexeme = nlp.vocab["coffee"]

print(lexeme.text, lexeme.orth, lexeme.is_alpha)
