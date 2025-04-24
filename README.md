# RDFMapper with Strategy Pattern and Web GUI

This project implements a flexible RDF conversion tool using the **Strategy Design Pattern** in Python. It supports parsing data from multiple input formats (JSON, XML, SQL) and converting them into RDF or OWL-compatible formats using `rdflib`. A lightweight HTML GUI is provided using Flask, making it accessible from a web browser.

---

## Features
- ✅ Strategy Pattern for easy extensibility
- ✅ Input support for JSON, XML, and SQLite
- ✅ RDF conversion using `rdflib`
- ✅ Flask GUI for interactive usage in a browser

---

## Requirements
Install required packages:
```bash
pip install -r requirements.txt
```

---

## How to Use
1. **Run the Flask server**:
```bash
python rdf_mapper.py
```
2. **Navigate to** `http://127.0.0.1:5000/` in your browser.
3. **Upload your file**, choose input type, and generate RDF output.

---

## Supported Input Types
- **JSON**: Well-formed JSON documents.
- **XML**: Basic XML format (you may extend the parser for complex schemas).
- **SQLite**: Expects a `some_table` table in the `.db` file. Customize as needed.

---

## To Do
- [ ] Add support for OWL output
- [ ] Improve ontology generation logic
- [ ] Enhance GUI with HTML templates and styling
- [ ] Add unit tests

---

## License
MIT License

---

## Contributing
Pull requests welcome! For major changes, please open an issue first to discuss what you would like to change.

## Examples
This repository includes example input files in the samples/ directory:


Format	File	Description
JSON	sample.json	Array of patient objects
XML	sample.xml	Same patient data in XML format
SQLite	sample.db	patients table with 2 rows
OWL/RDF	sample.owl	Minimal ontology describing patients
To test the system:

Launch the app (python app.py)

Upload one of the sample files via the web interface

View the converted RDF output
