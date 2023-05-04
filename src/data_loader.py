import json


class DataLoader:
    def __init__(self, data_path):
        self.data_path = data_path

    def load_data(self):
        """Loads the entire dataset into memory."""
        with open(self.data_path, 'r') as f:
            data = json.load(f)
        return data

    def get_examples(self):
        """A generator that yields examples one at a time to avoid loading the entire dataset into memory."""
        with open(self.data_path, 'r') as f:
            data = json.load(f)
            for article in data['data']:
                for paragraph in article['paragraphs']:
                    context = paragraph['context']
                    for qa in paragraph['qas']:
                        question = qa['question']
                        answers = [ans['text'] for ans in qa['answers']]
                        yield {
                            'context': context,
                            'question': question,
                            'answers': answers
                        }


if __name__ == '__main__':
    # Example usage
    data_loader = DataLoader('data/sample.json')

    # Using the get_examples generator
    for example in data_loader.get_examples():
        print(f"Context: {example['context'][:50]}...")  # Print only the first 50 characters
        print(f"Question: {example['question']}")
        print(f"Answers: {example['answers']}")
        break  # Only process the first example