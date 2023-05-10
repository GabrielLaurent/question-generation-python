import nltk.translate.bleu_score as bleu

def calculate_bleu(generated_questions, reference_answers):
    '''
    Calculates the BLEU score for the generated questions against the reference answers.

    Args:
        generated_questions: A list of generated questions (strings).
        reference_answers: A list of reference answers (strings).

    Returns:
        The average BLEU score.
    '''
    if not generated_questions or not reference_answers:
        return 0.0

    bleu_scores = []
    for question, answer in zip(generated_questions, reference_answers):
        # Tokenize the question and answer
        question_tokens = question.split()
        answer_tokens = answer.split()

        # Calculate BLEU score (using BLEU-1 for simplicity)
        if len(answer_tokens) > 0:
            score = bleu.sentence_bleu([answer_tokens], question_tokens, weights=(1.0,))
            bleu_scores.append(score)
        else:
            bleu_scores.append(0.0) # Handle the case where the reference answer is empty.


    # Calculate the average BLEU score
    if bleu_scores:
        avg_bleu_score = sum(bleu_scores) / len(bleu_scores)
    else:
        avg_bleu_score = 0.0

    return avg_bleu_score