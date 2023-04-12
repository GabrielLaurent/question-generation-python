from transformers import pipeline
from src.logger import logger
from src.mlflow_utils import log_param, log_metric

class TransformerQuestionGenerator:
    def __init__(self, model_name='t5-small', device=0):
        self.model_name = model_name
        self.device = device  # 0 for GPU, -1 for CPU

        logger.info(f'Loading model {model_name} on device {device}')
        self.question_generator = pipeline('question-generation', model=model_name, device=device)
        logger.info('Model loaded successfully')

    def generate_question(self, context, answer):
        try:
            input_text = f"context: {context} answer: {answer}"
            log_param('input_text', input_text)
            question = self.question_generator(input_text)[0]['question']
            return question
        except Exception as e:
            logger.error(f'Error during question generation: {e}')
            return None


if __name__ == '__main__':
    # Example usage
    generator = TransformerQuestionGenerator()
    context = "The cat sat on the mat."
    answer = "mat"
    question = generator.generate_question(context, answer)

    if question:
        print(f"Context: {context}")
        print(f"Answer: {answer}")
        print(f"Question: {question}")
    else:
        print("No question could be generated.")