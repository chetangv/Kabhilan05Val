
import json
# Load commands from the JSON file
def load_commands_from_json(file_path):
    """Load commands and their expected outputs from a JSON file."""
    with open(file_path, 'r') as file:
        return json.load(file)