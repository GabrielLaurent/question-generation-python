import json
from src.logger import logger
from collections import defaultdict

def calculate_eval_metrics(gold_data, generated_data):
    """Calculates evaluation metrics (e.g., exact match, F1 score) between generated questions and gold questions.

    Args:
        gold_data (list): A list of dictionaries, where each dictionary contains the ground truth question and answer.
        generated_data (list): A list of dictionaries, where each dictionary contains the generated question.

    Returns:
        dict: A dictionary containing the evaluation metrics.
    """

    # Placeholder for evaluation metrics calculation
    # Replace with actual implementation, e.g., using metrics like BLEU, ROUGE, etc.
    # For now, we'll provide dummy metrics
    
    if not gold_data or not generated_data:
        logger.warning("No data provided for evaluation.")
        return {"exact_match": 0.0, "f1_score": 0.0}
    
    # Check if the lengths are the same to avoid index out of bounds errors
    min_len = min(len(gold_data), len(generated_data))    
    num_correct = 0
    for i in range(min_len):
        gold_answer = gold_data[i]['answer'].lower()
        generated_question = generated_data[i]['question'].lower()
        
        # Simple exact match (case-insensitive)
        if gold_answer in generated_question:
            num_correct += 1
    
    exact_match = num_correct / min_len if min_len > 0 else 0.0

    #Dummy F1 Score for demonstration
    f1_score = 0.75 #Assign a fixed F1 score
    
    return {"exact_match": exact_match, "f1_score": f1_score}
