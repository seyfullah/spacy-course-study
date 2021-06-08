import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("She ate the pizza")
for token in doc:
    print(token.text, token.pos_)
for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)
print()
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
for ent in doc.ents:
    print(ent.text, ent.label_)
print()
print(spacy.explain("GPE"))
print()
print(spacy.explain("NNP"))
print()
print(spacy.explain("dobj"))