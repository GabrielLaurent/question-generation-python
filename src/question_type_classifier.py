import nltk
import random
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
import joblib

class QuestionTypeClassifier:
    def __init__(self, model_path='question_type_model.joblib'):
        self.model_path = model_path
        self.model = None
        self.vectorizer = None
        self.categories = None # Store the categories learned from training

    def train(self, data, labels):
        # data is a list of contexts, labels are question types for each context
        self.categories = list(set(labels)) # Extract categories for classification
        self.model = Pipeline([('tfidf', TfidfVectorizer()), ('clf', MultinomialNB())])
        self.model.fit(data, labels)

    def predict(self, text):
        if self.model is None:
            raise ValueError("Model not trained. Call train() first.")
        return self.model.predict([text])[0]

    def save(self):
        if self.model:
            joblib.dump(self.model, self.model_path)

    def load(self):
        try:
            self.model = joblib.load(self.model_path)
            # Infer categories from the saved model (if possible, TFIDF might not store it directly)
            # Consider storing categories separately when saving the model in the future for clarity
            # This depends on the specifics of sklearn version and serialization. To avoid dependency,
            # we force the user to retrain or explicitly define the categories if model is reloaded.
            # self.categories = list(self.model['clf'].classes_)
            print('Model loaded successfully.')
        except FileNotFoundError:
            print('No saved model found. Please train the model first.')


if __name__ == '__main__':
    # Example Usage for Training (replace with your actual data)
    contexts = [
        "The cat sat on the mat.",
        "The dog barked loudly.",
        "The sun is shining.",
        "Water is essential for life."  # Added explicit context
    ]
    question_types = [
        "Simple",
        "Simple",
        "Simple",
        "Complex" # Added question type that isn't just 'simple'
    ]

    # Split the data
    train_contexts, test_contexts, train_types, test_types = train_test_split(contexts, question_types, test_size=0.2, random_state=42)

    classifier = QuestionTypeClassifier()
    classifier.train(train_contexts, train_types)
    classifier.save()

    # Load the model and test it
    classifier.load()
    example_text = "The cat is sleeping."
    predicted_type = classifier.predict(example_text)
    print(f"Predicted type for '{example_text}': {predicted_type}")
