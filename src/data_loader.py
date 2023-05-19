import json

def load_data(file_path):
    """Loads data from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        list: A list of dictionaries, where each dictionary represents a data entry.
    """
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []  # Or raise the exception, depending on desired behavior
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {file_path}")
        return [] # Or raise the exception, depending on desired behavior
