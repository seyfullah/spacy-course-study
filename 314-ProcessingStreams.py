import json
import spacy
nlp = spacy.load("en_core_web_sm")

with open("tweets.json", encoding="utf8") as f:
    TEXTS = json.loads(f.read())
    
# Process the texts and print the adjectives
for text in TEXTS:
    doc = nlp(text)
    print([token.text for token in doc if token.pos_ == "ADJ"])

for doc in nlp.pipe(TEXTS):
    print([token.text for token in doc if token.pos_ == "ADJ"])


import json
import spacy

nlp = spacy.load("en_core_web_sm")

with open("tweets.json", encoding="utf8") as f:
    TEXTS = json.loads(f.read())

# Process the texts and print the entities
docs = [nlp(text) for text in TEXTS]
entities = [doc.ents for doc in docs]
print(*entities)


docs = list(nlp.pipe(TEXTS))
entities = [doc.ents for doc in docs]
print(*entities)







from spacy.lang.en import English

nlp = English()

people = ["David Bowie", "Angela Merkel", "Lady Gaga"]

# Create a list of patterns for the PhraseMatcher
patterns = [nlp(person) for person in people]

patterns = list(nlp.pipe(people))