import logging

from src.logger import setup_logger

logger = setup_logger()

class RuleBasedQuestionGenerator:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.info("RuleBasedQuestionGenerator initialized")

    def generate_question(self, context, answer):
        # Very basic rule-based question generation
        self.logger.info(f"Generating question for answer: {answer}, context: {context}")
        return f"What is {answer} in the context of {context}?"
