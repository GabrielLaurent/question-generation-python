from src.logger import setup_logger

logger = setup_logger(__name__)

class RuleBasedQuestionGenerator:
    def __init__(self):
        logger.info('Initializing RuleBasedQuestionGenerator')

    def generate_question(self, context, answer):
        logger.info(f'Generating question for context: {context[:50]}... and answer: {answer}') # Truncate context for logging
        try:
            # Simple rule-based question generation (replace with your logic)
            question = f'What is the answer to this: {context}?'
            logger.debug(f'Generated question: {question}') # Log generated question for debug
            return question
        except Exception as e:
            logger.exception(f'An error occurred during question generation')
            raise e