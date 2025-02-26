import nbformat
from nbconvert.preprocessors import ClearOutputPreprocessor

# Pfad zum Notebook
notebook_filename = 'exercise.ipynb'

# Notebook laden
with open(notebook_filename, 'r', encoding='utf-8') as f:
    notebook = nbformat.read(f, as_version=4)

# ClearOutputPreprocessor anwenden
clear_output_preprocessor = ClearOutputPreprocessor()

# Outputs löschen
clear_output_preprocessor.preprocess(notebook, {})

# Geändertes Notebook speichern
with open(notebook_filename, 'w', encoding='utf-8') as f:
    nbformat.write(notebook, f)

print(f"Outputs in {notebook_filename} wurden gelöscht.")
