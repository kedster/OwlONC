
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

@app.route('/', methods=['GET', 'POST'])
def index():
    rdf_output = ""
    if request.method == 'POST':
        file = request.files['datafile']
        datatype = request.form['datatype']
        
        filepath = os.path.join("temp_input." + datatype)
        file.save(filepath)

        strategy = strategy_map.get(datatype)
        if strategy:
            data = strategy.load_data(filepath)
            rdf_output = generate_rdf(data)

        os.remove(filepath)

    return render_template("index.html", rdf_output=rdf_output)

if __name__ == '__main__':
    app.run(debug=True)
