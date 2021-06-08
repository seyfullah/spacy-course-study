import spacy

nlp = spacy.load("en_core_web_sm")
text = (
    "Chick-fil-A is an American fast food restaurant chain headquartered in "
    "the city of College Park, Georgia, specializing in chicken sandwiches."
)

# Only tokenize the text
doc = nlp.make_doc(text)
print([token.text for token in doc])


import spacy

nlp = spacy.load("en_core_web_sm")
text = (
    "Chick-fil-A is an American fast food restaurant chain headquartered in "
    "the city of College Park, Georgia, specializing in chicken sandwiches."
)

# # # Disable the tagger and parser
# # with nlp.disable_pipes("tagger", "parser"):
# with nlp.select_pipes(disable=["tagger", "parser"]):
#     # Process the text
#     doc = nlp(text)
# #     # Print the entities in the doc
# #     print(doc.ents)

with nlp.select_pipes(disable=["tagger", "parser"]):
    nlp.initialize()

with nlp.select_pipes(enable="ner"):
    nlp.initialize()

disabled = nlp.select_pipes(disable=["tagger", "parser"])
nlp.initialize()
# Process the text
doc = nlp(text)
# Print the entities in the doc
print(doc.ents)   

disabled.restore()