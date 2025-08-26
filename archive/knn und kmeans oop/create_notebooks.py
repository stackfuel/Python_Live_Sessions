import nbformat
from nbconvert.preprocessors import ExecutePreprocessor, TagRemovePreprocessor

# Pfad zum Original-Notebook
notebook_filename = 'working.ipynb'

# Notebook laden
with open(notebook_filename, 'r', encoding='utf-8') as f:
    notebook = nbformat.read(f, as_version=4)

# Preprocessor für das Entfernen von Zellen mit bestimmten Tags erstellen
trp_exercise = TagRemovePreprocessor(remove_cell_tags=["exercise"])
trp_solution = TagRemovePreprocessor(remove_cell_tags=["solution"])

# Preprocessor für das Ausführen von Notebooks erstellen
ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

# Zellen mit dem Tag "exercise" entfernen und als "solution.ipynb" speichern
notebook_solution = trp_exercise.preprocess(notebook, {})
with open('solution.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(notebook_solution[0], f)

# "solution.ipynb" ausführen
with open('solution.ipynb', 'r', encoding='utf-8') as f:
    notebook = nbformat.read(f, as_version=4)
ep.preprocess(notebook, {'metadata': {'path': './'}})
with open('solution.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(notebook, f)

# Zellen mit dem Tag "solution" entfernen und als "exercise.ipynb" speichern
notebook_exercise = trp_solution.preprocess(notebook, {})
with open('exercise.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(notebook_exercise[0], f)
