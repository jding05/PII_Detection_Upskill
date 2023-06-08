import spacy

class PIIEntity:
    def __init__(self, entity_type, text, start_index, end_index):
        self.entity_type = entity_type
        self.text = text
        self.start_index = start_index
        self.end_index = end_index

def replace_pii(text):
    
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)

    pii_entities = []
    modified_text = text
    offset = 0

    for ent in doc.ents:
        if ent.label_ == "PERSON" or ent.label_ == "GPE" or ent.label_ == "CARDINAL":
            pii_entity = PIIEntity(
                entity_type=ent.label_,
                text=ent.text,
                start_index=ent.start_char,
                end_index=ent.end_char - 1
            )
            pii_entities.append(pii_entity)
            modified_text = modified_text[:ent.start_char - offset] + "<PII>" + modified_text[ent.end_char - offset:]
            offset += len(ent.text) - len("<PII>")


    return modified_text, pii_entities


text = "John Doe lives at 123 Main Street, New York. His phone number is (555) 123-4567."
modified_text, pii_entities = replace_pii(text)

# Print the modified text with replaced PII entities
print("Modified Text:", modified_text)

# Print the extracted PII entities
print("Extracted PII Entities:")
for pii_entity in pii_entities:
    print("Type:", pii_entity.entity_type)
    print("Value:", pii_entity.text)
    print("Start Index:", pii_entity.start_index)
    print("End Index:", pii_entity.end_index)
    print("---")