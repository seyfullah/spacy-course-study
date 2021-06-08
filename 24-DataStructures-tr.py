from spacy.lang.tr import Turkish
nlp = Turkish()

# Import the Doc and Span classes
from spacy.tokens import Doc, Span

# The words and spaces to create the doc from
words = ["Merhaba", "Dünya", "!"]
spaces = [True, False, False]

# Create a doc manually
doc = Doc(nlp.vocab, words=words, spaces=spaces)

# Create a span manually
span = Span(doc, 0, 2)

# Create a span with a label
span_with_label = Span(doc, 0, 2, label="SELAMLAMA")

# Add span to the doc.ents
doc.ents = [span_with_label]
print(doc)