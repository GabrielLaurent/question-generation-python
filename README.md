# Question Generation

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
<!-- Add more badges as needed, e.g., build status, code coverage -->

## Project Overview

This project aims to build a system that can automatically generate questions from a given context, similar to the functionality of datasets like SQuAD. The initial focus is on establishing a solid foundation with data loading, a basic rule-based question generation model, and preliminary evaluation metrics. Later phases will explore more advanced techniques using transformers and integrate experiment tracking with MLflow.

### Key Features

*   **Data Loading:** Efficient loading and preprocessing of datasets.
*   **Question Generation Models:**
    *   Rule-based question generation (initial implementation).
    *   Future implementations will include transformer-based models.
*   **Evaluation Metrics:**  Implementation of metrics for evaluating the quality of generated questions.
*   **Experiment Tracking:** Integration with MLflow to track experiments, parameters, and results.
*   **Modular Architecture:** Designed for easy extension and experimentation with different models and techniques.

### Project Goals

*   Develop a robust question generation system.
*   Provide a platform for experimenting with different question generation models.
*   Benchmark and evaluate the performance of different models.
*   Facilitate research in question generation.

## Installation

### Prerequisites

*   Python 3.7 or higher
*   pip package manager

### Installation Steps

1.  **Clone the repository:**

    ```bash
    git clone <your_repository_url>
    cd question_generation
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate.bat # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Basic Usage

1.  **Data Preparation:** Put your dataset (e.g., a JSON file similar to SQuAD) into the `data` directory.

2.  **Running the Rule-Based Generator:**

    ```python
    from src.data_loader.data_loader import load_data
    from src.question_generation.rule_based_generator import RuleBasedQuestionGenerator
    from src.evaluation.eval_metrics import simple_metrics

    # Load data
    context = "The cat sat on the mat."
    answer = "mat"
    data = [{"context": context, "answer": answer}] # create a mocked data sample for demonstration

    # Initialize question generator
    generator = RuleBasedQuestionGenerator()

    # Generate questions
    questions = generator.generate(data)

    # Evaluate
    print(f"Generated questions: {questions}")

    data_with_questions = [{"context": context, "answer": answer, "question": questions[0]}]
    metrics = simple_metrics(data_with_questions)

    print(f"Metrics: {metrics}")

    ```

    Modify the above script as necessary, making sure to change the mocked data sample with a data loader if preferred.
    You can then create a script within `src/` to execute such workflow.
    This is a very simple example, and usage will become more sophisticated as the project evolves, consider `src/main.py` or similar.
3.  **Running tests**

    ```
    pytest
    ```

### Configuration

Configuration files (e.g., `.yaml` or `.json`) will be introduced in later phases to manage parameters for models, data loading, and other components. For the initial phase, configurations are managed directly in the source code.

### Examples

More detailed examples will be provided in the `notebooks` directory as the project progresses. These notebooks will demonstrate how to load and preprocess data, train and evaluate models, and track experiments with MLflow.

## Project Structure

```
question_generation/
├── data/                           # Datasets for training and evaluation
├── src/                            # Source code
│   ├── data_loader/                # Data loading and preprocessing modules
│   │   ├── data_loader.py           # Module for loading and preprocessing data
│   │   └── ...
│   ├── question_generation/        # Question generation models
│   │   ├── rule_based_generator.py # Implementation of a rule-based question generator
│   │   └── ...
│   ├── evaluation/                 # Evaluation modules
│   │   ├── eval_metrics.py          # Implementation of evaluation metrics
│   │   └── ...
│   ├── utils/                      # Utility functions and helper classes
│   │   ├── logger.py                # Logging utility
│   │   └── ...
│   └── ...
├── models/                         # Trained models (will be populated later)
├── notebooks/                      # Jupyter notebooks for experimentation and analysis
│   ├── data_exploration.ipynb       # Notebook for data exploration
│   └── ...
├── tests/                          # Unit and integration tests
│   ├── test_data_loader.py        # Unit tests for data loading
│   ├── test_rule_based_generator.py # Unit tests for rule-based generator
│   └── ...
├── .gitignore                      # Specifies intentionally untracked files Git should ignore
├── README.md                       # Project documentation
└── requirements.txt                # Project dependencies
```

### Key Files and Their Purposes

*   **`README.md`:**  This file, containing project documentation and instructions.
*   **`requirements.txt`:**  Lists the project dependencies.
*   **`.gitignore`:**  Specifies intentionally untracked files that Git should ignore.
*   **`src/data_loader/data_loader.py`:**  Module for loading and preprocessing data.
*   **`src/question_generation/rule_based_generator.py`:** Implementation of a rule-based question generation model.
*   **`src/evaluation/eval_metrics.py`:** Implementation of evaluation metrics.
*   **`src/utils/logger.py`:** Logging utility.
*   **`tests/test_data_loader.py`:** Unit tests for the data loading module.
*   **`tests/test_rule_based_generator.py`:** Unit tests for the rule based generator.
*   **`notebooks/data_exploration.ipynb`:** Jupyter notebook for data exploration.

## Development

### Development Setup

1.  **Fork the repository** on GitHub.
2.  **Clone your forked repository** to your local machine.
3.  **Set up a development environment** using a virtual environment (as described in the Installation section).
4.  **Install the development dependencies:** `pip install -r requirements.txt` (ensure all testing and linting libraries are here!)
5.  **Configure your editor** to use appropriate linting and formatting tools (e.g., pylint, black).

### Contributing Guidelines

1.  **Create a new branch** for your feature or bug fix.
2.  **Implement your changes** following the project's coding style.
3.  **Write unit tests** to ensure the quality of your code.
4.  **Update documentation** to reflect your code changes.
5.  **Run tests**

    ```bash
    pytest tests/
    ```

6.  **Commit your changes** with a clear and concise commit message.
7.  **Push your branch** to your forked repository on GitHub.
8.  **Submit a pull request** to the main repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

*   This project is inspired by the Stanford Question Answering Dataset (SQuAD).
*   We acknowledge the contributions of the open-source community to the libraries and tools used in this project.