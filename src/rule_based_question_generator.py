import random
from src.question_type_classifier import QuestionTypeClassifier

class RuleBasedQuestionGenerator:
    def __init__(self, question_type_model_path='question_type_model.joblib'):
        self.question_type_classifier = QuestionTypeClassifier(question_type_model_path)
        try:
            self.question_type_classifier.load()
        except FileNotFoundError:
            print("Question type classifier model not found. Make sure it is trained and saved.")
            self.question_type_classifier = None

    def generate_question(self, context, answer):
        if self.question_type_classifier is None:
            return "Question generation disabled until the question type classifier is available.", False

        question_type = self.question_type_classifier.predict(context)

        if question_type == "Simple":
            question = f"What about {answer}?"
        elif question_type == "Complex":
            question = f"Considering the context, how does {answer} relate?"
        else:
            question = f"Tell me more about {answer}."

        return question, True


if __name__ == '__main__':
    # Example Usage
    context = "The quick brown fox jumps over the lazy dog."
    answer = "the quick brown fox"

    generator = RuleBasedQuestionGenerator()
    question, success = generator.generate_question(context, answer)
    print(f"Generated question: {question}, Success: {success}")
