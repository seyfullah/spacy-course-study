import spacy

# Import the Matcher
from spacy.matcher import Matcher

# Load a model and create the nlp object
nlp = spacy.load("en_core_web_sm")

# Add the pattern to the matcher
pattern = [{"TEXT": "iPhone"}, {"TEXT": "X"}]

# Process some text
doc = nlp("Upcoming iPhone X release date leaked")

def print_doc(doc, pattern):
    # Initialize the matcher with the shared vocab
    matcher = Matcher(nlp.vocab)
    matcher.add("mypattern", [pattern])
    # Call the matcher on the doc
    matches = matcher(doc)

    for match_id, start, end in matches:
        matched_span = doc[start:end]
        print(match_id, start, end)
        print(matched_span)
        print()

print_doc(doc, pattern)

pattern = [
    {"IS_DIGIT":True},
    {"LOWER":"fifa"},
    {"LOWER":"world"},
    {"LOWER":"cup"},
    {"IS_PUNCT":True}
]
doc = nlp("2018 FIFA World Cup: France won!")
print_doc(doc, pattern)

pattern = [
    {"LEMMA":"love", "POS": "VERB"},
    {"POS":"NOUN"}
]

doc = nlp("I loved dogs but now I love cats more.")
print_doc(doc, pattern)

pattern = [
    {"LEMMA": "buy"},
    {"POS": "DET", "OP":"?"},
    {"POS": "NOUN"}
]
doc = nlp("I bought a smartphone. Now I'm buying apps.")
print_doc(doc, pattern)