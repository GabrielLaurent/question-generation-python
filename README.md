# question_generation

This project focuses on question generation, likely based on a dataset similar to SQuAD. The architecture is research-oriented, emphasizing experimentation and flexibility. The development plan focuses on recreating a simplified version of the project, prioritizing core functionality like data loading, basic question generation, and evaluation, before adding more advanced features.

## Setup

1.  Clone the repository:
    ```bash
    git clone <repository_url>
    cd question_generation
    ```

2.  Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  Install the dependencies.  Since no dependencies were initially specified, I'll assume a need for requests:
    ```bash
    pip install requests # a very common library for quick testing
    ```

## Usage

1.  Navigate to the `src` directory:
    ```bash
    cd src
    ```

2.  Run the desired script (e.g., `rule_based_question_generator.py`):
    ```bash
    python rule_based_question_generator.py
    ```

## Project Structure

```
question_generation/
├── data/
│   └── sample.json          # Sample data (SQuAD-like format)
├── src/
│   ├── data_loader.py       # Loads and preprocesses data
│   ├── evaluation.py        # Evaluates question generation performance
│   ├── logger.py            # Handles logging functionality
│   ├── rule_based_question_generator.py # Generates questions using rule-based approaches
│   ├── test_data_loader.py  # Unit tests for data_loader.py
│   ├── test_evaluation.py   # Unit tests for evaluation.py
│   └── test_rule_based_question_generator.py # Unit tests for rule_based_question_generator.py
├── .gitignore
└── README.md
```

## Documentation

Refer to the docstrings within each Python file for detailed information on functions and classes.
