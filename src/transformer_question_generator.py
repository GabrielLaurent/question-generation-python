import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer, Trainer, TrainingArguments
from torch.utils.data import Dataset
import json

class QGDataset(Dataset):
    def __init__(self, data, tokenizer, max_length=512):
        self.data = data
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]
        context = item['context']
        answer = item['answer']

        # Input text: context + answer
        input_text = f"generate question: context: {context} answer: {answer}"
        target_text = item['question']

        input_encoding = self.tokenizer(input_text, padding='max_length', truncation=True, max_length=self.max_length, return_tensors='pt')
        target_encoding = self.tokenizer(target_text, padding='max_length', truncation=True, max_length=self.max_length, return_tensors='pt')

        labels = target_encoding['input_ids']
        labels[labels == self.tokenizer.pad_token_id] = -100 # CrossEntropyLoss ignores index -100

        return {
            'input_ids': input_encoding['input_ids'].flatten(),
            'attention_mask': input_encoding['attention_mask'].flatten(),
            'labels': labels.flatten()
        }


class TransformerQuestionGenerator:
    def __init__(self, model_name='t5-small', data_path='data/sample.json', output_dir='output', epochs=1):
        self.model_name = model_name
        self.data_path = data_path
        self.output_dir = output_dir
        self.epochs = epochs
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.tokenizer = T5Tokenizer.from_pretrained(self.model_name)
        self.model = T5ForConditionalGeneration.from_pretrained(self.model_name).to(self.device)

    def load_data(self):
        with open(self.data_path, 'r') as f:
            data = json.load(f)
        return data

    def train(self):
        data = self.load_data()
        train_dataset = QGDataset(data, self.tokenizer)

        training_args = TrainingArguments(
            output_dir=self.output_dir,
            per_device_train_batch_size=8,
            num_train_epochs=self.epochs,
            logging_dir='./logs',
            save_strategy='epoch'
        )

        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=train_dataset,
            tokenizer=self.tokenizer
        )

        trainer.train()

    def generate_question(self, context, answer, max_length=64):
        input_text = f"generate question: context: {context} answer: {answer}"
        input_ids = self.tokenizer.encode(input_text, return_tensors='pt').to(self.device)

        output = self.model.generate(input_ids, max_length=max_length)
        question = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return question