import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# English text to analyze
text_sample = "Yesterday, Alice and Bob visited Paris to buy a new smartphone from Apple."

# Process the text
doc = nlp(text_sample)

# Analyze the text
print("Tokens and their parts of speech:")
print("---GRAMMAR AND MORPHOLOGY ANALYSIS---")
for token in doc:
    #token.pos_ gives the part of speech tag for each token (e.g., noun, verb, adjective)
    #token.morph gives the morphological features of the token (e.g., tense, number, case)
    print(f"Word: '{token.text:<15}' | Category: {token.pos_:<10}, Morphology details: {token.morph}")
print("\n---ENTITY ANALYSIS (NAMED ENTITY RECOGNITION)---")
for ent in doc.ents:
    #ent.text gives the text of the entity, and ent.label_ gives the type of entity (e.g., PERSON, ORG, GPE)
    print(f"Entity: '{ent.text:<15}' | Label: {ent.label_}")