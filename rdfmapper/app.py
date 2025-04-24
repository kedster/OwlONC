```python
from flask import Flask, render_template, request
from strategies.json_strategy import JSONStrategy
from strategies.xml_strategy import XMLStrategy
from strategies.sql_strategy import SQLStrategy
from rdf_mapper import generate_rdf
import os

app = Flask(__name__)

strategy_map = {
    'json': JSONStrategy(),
    'xml': XMLStrategy(),
    'sql': SQLStrategy()
}
