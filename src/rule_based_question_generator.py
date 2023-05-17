import re

def generate_question(text):
    # Simple regex to identify named entities (very basic)
    entities = re.findall(r'[A-Z][a-z]+', text)
    
    if not entities:
        return []

    questions = []
    for entity in entities:
        questions.append(f"What is {entity}?"
    
    return questions

if __name__ == '__main__':
    text = "Barack Obama was the 44th President of the United States."
    questions = generate_question(text)
    for question in questions:
        print(question)