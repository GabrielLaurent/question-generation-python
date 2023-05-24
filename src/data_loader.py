import json

def load_data(filepath):
    """Loads and preprocesses SQuAD data from a JSON file.

    Args:
        filepath (str): The path to the JSON file containing the SQuAD data.

    Returns:
        list: A list of dictionaries, where each dictionary represents a
              question-answer pair with context.
    """
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)

        # Accessing the data structure based on the SQuAD format
        data_list = []
        for article in data['data']:
            for paragraph in article['paragraphs']:
                for qa in paragraph['qas']:
                    question = qa['question']
                    answers = qa['answers']  # List of answers
                    context = paragraph['context']
                    data_list.append({
                        'question': question,
                        'answers': answers,
                        'context': context
                    })
        return data_list
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return []
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {filepath}")
        return []
    except KeyError as e:
        print(f"Error: Incorrect SQuAD data structure. Missing key: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

if __name__ == '__main__':
    # Example usage (assuming dummy_data.json is in the correct relative path)
    filepath = 'data/squad_multitask/dummy/plain_text/1.0.0/dummy_data/dummy_data.json'
    data = load_data(filepath)
    if data:
        print(f"Loaded {len(data)} question-answer pairs.")
        # Print the first question and its first answer for verification
        print(f"Question: {data[0]['question']}")
        print(f"Answer: {data[0]['answers'][0]['text'] if data[0]['answers'] else 'No answer provided'}")