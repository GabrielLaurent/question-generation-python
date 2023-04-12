import json
import random
from src.logger import logger
import os
from src.mlflow_utils import log_param, log_metric

class RuleBasedQuestionGenerator:
    def __init__(self, rules_file='data/rules.json'):
        self.rules = self.load_rules(rules_file)
        logger.info(f'Loaded rules from {rules_file}')

    def load_rules(self, rules_file):
        with open(rules_file, 'r') as f:
            rules = json.load(f)
        return rules

    def generate_question(self, context, answer):
        possible_rules = []
        for rule_name, rule_data in self.rules.items():
            if rule_data['answer_type'] == self.get_answer_type(answer):
                possible_rules.append((rule_name, rule_data))

        if not possible_rules:
            return None  # No suitable rule found

        rule_name, rule_data = random.choice(possible_rules)

        question = rule_data['template'].replace('ANS', answer)
        question = question.replace('CTX', context)
        log_param('used_rule', rule_name)
        return question

    def get_answer_type(self, answer):
        # Basic answer type detection (can be extended)
        if answer.isdigit():
            return 'number'
        else:
            return 'text'


if __name__ == '__main__':
    # Example usage
    generator = RuleBasedQuestionGenerator()
    context = "The cat sat on the mat."
    answer = "mat"
    question = generator.generate_question(context, answer)

    if question:
        print(f"Context: {context}")
        print(f"Answer: {answer}")
        print(f"Question: {question}")
    else:
        print("No question could be generated.")