from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

# Initialize the analyzer and anonymizer engines
analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

class PIIEntity:
    def __init__(self, entity_type, text, start_index, end_index):
        self.entity_type = entity_type
        self.text = text
        self.start_index = start_index
        self.end_index = end_index

def extract_pii(text, analysis_results):
    # Extract the identified PII entities from the analysis results
    pii_entities = []
    for result in analysis_results:
        pii_entity = PIIEntity(
            entity_type=result.entity_type,
            text=text[result.start:result.end],
            start_index=result.start,
            end_index=result.end
        )
        pii_entities.append(pii_entity)

    return pii_entities

def print_piiEntity(text, pii_entities):
    print("original text:" + text)
    print("--------")
    for pii_entity in pii_entities:
        print("Type:", pii_entity.entity_type)
        print("Value:", pii_entity.text)
        print("Start Index:", pii_entity.start_index)
        print("End Index:", pii_entity.end_index)
        print("-----------------")

def remove_pii(text):
    # Analyze the text to identify PII entities
    analysis_results = analyzer.analyze(text=text,language='en')
    # print(analysis_results)

    pii_entity = extract_pii(text, analysis_results)
    print_piiEntity(text, pii_entity)

    redacted_text = anonymizer.anonymize(text, analysis_results)
    print("Redacted_text from Presidio Anonymize")
    print(redacted_text)
    print("-------------")
    return redacted_text.text

# Example usage
text = "John Doe lives in New York. His email is johndoe@example.com."
redacted_text = remove_pii(text)
print("Final Answer:")
print(redacted_text)