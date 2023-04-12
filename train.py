import json
import random
from src.data_loader import DataLoader
from src.rule_based_question_generator import RuleBasedQuestionGenerator
from src.transformer_question_generator import TransformerQuestionGenerator
from src.mlflow_utils import setup_mlflow, log_param, log_metric
import mlflow 


def main():
    # Initialize Mlflow
    run_id = setup_mlflow(experiment_name='Question Generation', run_name='Training Run')
    log_param('data_path', 'data/sample.json')
    log_param('model_type', 'rule_based')

    # Load Data
    data_loader = DataLoader()
    examples = data_loader.get_examples(num_examples=10)

    # Initialize Question Generator (choose one)
    #question_generator = RuleBasedQuestionGenerator()
    question_generator = TransformerQuestionGenerator()

    # Training Loop (simplified)
    for i, example in enumerate(examples):
        context = example['context']
        answer = example['answer']

        question = question_generator.generate_question(context, answer)

        if question:
            print(f"Context: {context}")
            print(f"Answer: {answer}")
            print(f"Question: {question}")
        else:
            print("No question could be generated.")

        # Log metrics (example)
        log_metric('training_step', i)
        #if i%5 == 0:
        #  mlflow.log_artifact('data/sample.json')

    mlflow.end_run()

if __name__ == "__main__":
    main()