import spacy
import random


nlp = spacy.load('en_core_web_sm')


class RuleBasedQuestionGenerator:
    def __init__(self):
        pass  # Initialize any necessary resources here

    def generate_question(self, context, answer):
        """Generates a question based on the given context and answer using rule-based techniques."""
        doc = nlp(context)
        answer_doc = nlp(answer)

        # Simple rule: What is the answer?
        question = f"What is {answer}?"
        return question

    def generate_questions_for_example(self, context, answers):
        """Generates a list of questions for a single context and list of potential answers."""
        questions = []
        for answer in answers:
            question = self.generate_question(context, answer)
            questions.append(question)
        return questions


if __name__ == '__main__':
    # Example Usage
    generator = RuleBasedQuestionGenerator()
    context = "The cat sat on the mat."
    answers = ["cat", "mat"]
    questions = generator.generate_questions_for_example(context, answers)
    for question in questions:
        print(question)
