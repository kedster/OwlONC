```python
from abc import ABC, abstractmethod

class DataInputStrategy(ABC):
    @abstractmethod
    def load_data(self, filepath):
        pass
