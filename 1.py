from spacy.lang.en import English

nlp = English()

doc = nlp("Hello World!")
for token in doc:
    print(token.text)

token = doc[1]
print(token.text)

span = doc[1:3]
print(span.text)
