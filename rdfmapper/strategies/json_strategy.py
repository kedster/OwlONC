
import json
from strategies.base import DataInputStrategy

class JSONStrategy(DataInputStrategy):
    def load_data(self, filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
