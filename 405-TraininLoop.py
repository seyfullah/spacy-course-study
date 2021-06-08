import spacy
import random
import json

# Create a blank "en" model
nlp = spacy.blank("en")

# Create a new entity recognizer and add it to the pipeline
ner = nlp.create_pipe("ner")
nlp.add_pipe("ner")

# Add the label "GADGET" to the entity recognizer
ner.add_label("GADGET")


with open("gadgets.json", encoding="utf8") as f:
    TRAINING_DATA = json.loads(f.read())


# Start the training
nlp.begin_training()

# Loop for 10 iterations
for itn in range(10):
    # Shuffle the training data
    random.shuffle(TRAINING_DATA)
    losses = {}

    # Batch the examples and iterate over them
    for batch in spacy.util.minibatch(TRAINING_DATA, size=2):
        texts = [text for text, entities in batch]
        annotations = [entities for text, entities in batch]

        # Update the model
        # nlp.update(texts, annotations, losses=losses)
    #     example = Example.from_dict(nlp.make_doc(text), annotations)
    #     nlp.update([example])


    # for raw_text, entity_offsets in TRAINING_DATA:
    #     doc = nlp.make_doc(raw_text)
    #     example = Example.from_dict(doc, {"entities": entity_offsets})
    #     nlp.update([example], sgd=optimizer)        
    print(losses)