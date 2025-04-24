
import xml.etree.ElementTree as ET
from strategies.base import DataInputStrategy

class XMLStrategy(DataInputStrategy):
    def load_data(self, filepath):
        tree = ET.parse(filepath)
        root = tree.getroot()
        return [{child.tag: child.text for child in elem} for elem in root]
