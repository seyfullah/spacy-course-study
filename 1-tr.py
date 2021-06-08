from spacy.lang.tr import Turkish

nlp = Turkish()

doc = nlp("Merhaba Dünya!")
for token in doc:
    print(token.text)

token = doc[1]
print(token.text)

span = doc[1:3]
print(span.text)
