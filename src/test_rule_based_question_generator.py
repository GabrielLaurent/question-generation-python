import unittest
import logging
from io import StringIO

from src.rule_based_question_generator import RuleBasedQuestionGenerator
from src.logger import setup_logger

class TestRuleBasedQuestionGenerator(unittest.TestCase):

    def setUp(self):
        self.logger = setup_logger(__name__, level=logging.DEBUG)
        self.log_stream = StringIO()
        handler = logging.StreamHandler(self.log_stream)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def tearDown(self):
        for handler in self.logger.handlers[:]:
            self.logger.removeHandler(handler)
            handler.close()

    def test_generate_question(self):
        generator = RuleBasedQuestionGenerator()
        context = 'This is a test context.'
        answer = 'Test answer.'
        question = generator.generate_question(context, answer)
        self.assertIn('What is the answer', question)
        self.assertIn('Generating question', self.log_stream.getvalue())
        self.assertIn('Generated question', self.log_stream.getvalue())


if __name__ == '__main__':
    unittest.main()