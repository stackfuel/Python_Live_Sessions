# Ankündigungen

## Ankündigung kurz
"Refactoring"

In dieser Session befassen wir uns mit dem Refactoring von funktionstüchtigem Programmcode. Ihr lernt einige Techniken kennen, die euren Code verständlicher und anpassbarer machen und die generelle Codequalität verbessern.

## Ankündigung lang

<!--
TODO:
-->






# Schritt-für-Schritt Anleitung zum Refactoring des Sudoku-Solvers

Diese Anleitung führt durch den vollständigen Refactoring-Prozess, um den ursprünglichen Sudoku-Löser-Code ("matrix.py") in eine gut strukturierte, wartbare Version ("sudoku_solver.py") zu transformieren. Jeder Schritt baut auf dem vorherigen auf und sollte in der angegebenen Reihenfolge durchgeführt werden.

## Teil 1: Vorbereitung und Verbesserung der Namensgebung

### Schritt 1: Dateiumbenennung
```
matrix.py → sudoku_solver.py
```
Begründung: Der neue Dateiname beschreibt den Zweck des Programms besser.

### Schritt 2: Verbesserung der Variablennamen
1. Ändern Sie `matrix` zu `sudoku` oder `sudoku_board`
   ```python
   # Vorher
   matrix = np.array([...])
   
   # Nachher
   sudoku_board = np.array([...])
   ```

2. Ändern Sie `cells` zu `empty_cells`
   ```python
   # Vorher
   cells = [(i, j) for i in range(9) for j in range(9) if matrix[i][j] == 0]
   
   # Nachher
   empty_cells = [(i, j) for i in range(9) for j in range(9) if sudoku_board[i][j] == 0]
   ```

3. Ändern Sie `i` (als Zähler für `cells`) zu `backtrack_index`
   ```python
   # Vorher
   i = 0
   while i < len(cells):
       
   # Nachher
   backtrack_index = 0
   while backtrack_index < len(empty_cells):
   ```

4. Ändern Sie `x` zu `candidate`
   ```python
   # Vorher
   x = matrix[row][col] + 1
   
   # Nachher
   candidate = sudoku_board[row][col] + 1
   ```

5. Fassen Sie `row, col` als `current_empty_cell` zusammen
   ```python
   # Vorher
   row, col = cells[i]
   
   # Nachher
   current_empty_cell = empty_cells[backtrack_index]
   ```

## Teil 2: Funktionsextraktion

### Schritt 3: Extrahieren der Sudoku-Darstellungsfunktion
Extrahieren Sie den Code zur Anzeige des Sudokus in eine separate Funktion:

```python
def get_sudoku_string(sudoku):
    """
    Erzeugt eine lesbare Zeichenkettendarstellung eines Sudoku-Boards.
    
    Args:
        sudoku (numpy.ndarray): Ein 2D-Array, das das Sudoku-Board repräsentiert, wobei 0 eine leere Zelle darstellt.
    """
    lines = []
    for i in range(9):
        if i % 3 == 0 and i != 0:
            lines.append("-" * 21)

        formatted_row = []
        for j in range(0, 9, 3):
            block = " ".join(str(num) if num != 0 else '.' for num in sudoku[i, j:j+3])
            formatted_row.append(block)

        line = " | ".join(formatted_row)
        lines.append(line)

    return "\n".join(lines)
```

Ersetzen Sie alle direkten Ausgaben durch Aufrufe dieser Funktion:
```python
# Vorher
print("\n".join(lines))

# Nachher
print(get_sudoku_string(sudoku_board))
```

### Schritt 4: Extrahieren der Validierungsfunktion
Extrahieren Sie die Logik zur Überprüfung, ob eine Zahl an einer bestimmten Position gültig ist:

```python
def is_valid(sudoku, number, position):
    """
    Prüft, ob eine gegebene Zahl an einer bestimmten Position auf einem Sudoku-Board platziert werden kann.
    
    Args:
        sudoku (numpy.ndarray): Ein 2D-Array, das das Sudoku-Board repräsentiert.
        number (int): Die Zahl, die auf dem Board platziert werden soll.
        position (tuple): Ein Tupel (row, col), das die Position auf dem Board repräsentiert.
    Returns:
        bool: True, wenn die Zahl an der gegebenen Position platziert werden kann, ohne die Sudoku-Regeln zu verletzen, False sonst.
    """
    row, col = position
    
    # Prüfen, ob die Nummer bereits in der Zeile vorhanden ist
    if number in sudoku[row, :]:
        return False
        
    # Prüfen, ob die Nummer bereits in der Spalte vorhanden ist
    if number in sudoku[:, col]:
        return False
        
    # Prüfen, ob die Nummer bereits im 3x3-Block vorhanden ist
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    if number in sudoku[start_row:start_row+3, start_col:start_col+3]:
        return False
        
    return True
```

### Schritt 5: Extrahieren der Lösungsfunktion
Extrahieren Sie den Hauptalgorithmus in eine separate Funktion:

```python
def solve_sudoku(sudoku):
    """
    Löst ein gegebenes Sudoku-Rätsel mit einem Backtracking-Algorithmus.
    
    Args:
        sudoku (numpy.ndarray): Ein 2D-Array, das das Sudoku-Board repräsentiert, wobei 0 eine leere Zelle darstellt.
    Returns:
        Eine 2D numpy.ndarray, die das gelöste Sudoku-Board repräsentiert.
    Raises:
        ValueError: Wenn keine Lösung für das gegebene Sudoku-Rätsel gefunden wird.
    """
    sudoku = sudoku.copy()  # Erstellen einer Kopie, um das Original nicht zu verändern
    empty_cells = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]
    
    backtrack_index = 0
    while backtrack_index < len(empty_cells):
        row, col = empty_cells[backtrack_index]
        current_value = sudoku[row][col]
        
        found = False
        for candidate in range(current_value + 1, 10):
            if is_valid(sudoku, candidate, (row, col)):
                sudoku[row][col] = candidate
                backtrack_index += 1
                found = True
                break
                
        if not found:
            sudoku[row][col] = 0
            backtrack_index -= 1
            if backtrack_index < 0:
                raise ValueError("Keine Lösung gefunden")
                
    return sudoku
```

### Schritt 6: Strukturieren des Hauptprogramms
Fügen Sie einen Main-Guard hinzu und strukturieren Sie das Hauptprogramm:

```python
if __name__ == "__main__":
    sudoku_board = np.array([
        [4, 0, 0, 9, 0, 0, 0, 5, 0],
        [0, 0, 5, 6, 0, 7, 2, 0, 4],
        [0, 0, 0, 0, 0, 4, 7, 0, 0],
        [8, 7, 0, 3, 0, 0, 6, 0, 0],
        [0, 0, 9, 7, 2, 0, 1, 8, 0],
        [0, 0, 6, 8, 9, 1, 0, 0, 0],
        [1, 0, 2, 4, 0, 0, 5, 6, 8],
        [7, 6, 0, 5, 3, 8, 0, 0, 1],
        [0, 0, 8, 0, 0, 2, 0, 7, 0]
    ])
    
    print("before")
    print(get_sudoku_string(sudoku_board))
    
    try:
        solved_board = solve_sudoku(sudoku_board)
        print("after")
        print(get_sudoku_string(solved_board))
    except ValueError as e:
        print(str(e))
```

## Teil 3: Optimierung und Verbesserung der Funktionen

### Schritt 7: Optimierung der Validierungsfunktion mit Sets
Verwenden Sie Sets für eine effizientere Implementierung der Validierungsprüfung:

```python
def is_valid(sudoku, number, position):
    """
    Prüft, ob eine gegebene Zahl an einer bestimmten Position auf einem Sudoku-Board platziert werden kann.
    
    Args:
        sudoku (numpy.ndarray): Ein 2D-Array, das das Sudoku-Board repräsentiert.
        number (int): Die Zahl, die auf dem Board platziert werden soll.
        position (tuple): Ein Tupel (row, col), das die Position auf dem Board repräsentiert.
    Returns:
        bool: True, wenn die Zahl an der gegebenen Position platziert werden kann, ohne die Sudoku-Regeln zu verletzen, False sonst.
    """
    row, col = position
    row_numbers = set(sudoku[row, :])
    col_numbers = set(sudoku[:, col])
    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    tile_numbers = set(sudoku[start_row:start_row+3, start_col:start_col+3].flatten())
    
    return number not in row_numbers | col_numbers | tile_numbers
```

### Schritt 8: Optimierung der Lösungsfunktion
1. Verwenden Sie den Python-spezifischen `else`-Block bei `for`-Schleifen für eine klarere Struktur:

```python
def solve_sudoku(sudoku):
    """
    Löst ein gegebenes Sudoku-Rätsel mit einem Backtracking-Algorithmus.
    
    Args:
        sudoku (numpy.ndarray): Ein 2D-Array, das das Sudoku-Board repräsentiert, wobei 0 eine leere Zelle darstellt.
    Returns:
        Eine 2D numpy.ndarray, die das gelöste Sudoku-Board repräsentiert.
    Raises:
        ValueError: Wenn keine Lösung für das gegebene Sudoku-Rätsel gefunden wird.
    """
    sudoku = sudoku.copy()
    empty_cells = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]
    
    backtrack_index = 0
    while backtrack_index < len(empty_cells):
        current_empty_cell = empty_cells[backtrack_index]
        
        for candidate in range(sudoku[current_empty_cell] + 1, 10):
            if is_valid(sudoku, candidate, current_empty_cell):
                sudoku[current_empty_cell] = candidate
                backtrack_index += 1
                break
        else:  # Dieser Block wird ausgeführt, wenn keine gültige Zahl gefunden wurde
            sudoku[current_empty_cell] = 0
            backtrack_index -= 1
            if backtrack_index < 0:
                raise ValueError("Keine Lösung gefunden")
                
    return sudoku
```

### Schritt 9: Hinzufügen von Argumentvalidierung in die Darstellungsfunktion
Fügen Sie Validierungschecks hinzu, um sicherzustellen, dass die Eingaben korrekt sind:

```python
def get_sudoku_string(sudoku):
    """
    Erzeugt eine lesbare Zeichenkettendarstellung eines Sudoku-Boards.
    
    Args:
        sudoku (numpy.ndarray): Ein 2D-Array, das das Sudoku-Board repräsentiert, wobei 0 eine leere Zelle darstellt.
    """
    if not isinstance(sudoku, np.ndarray):
        raise TypeError("Eingabe muss ein numpy ndarray sein.")
    if sudoku.shape != (9, 9):
        raise ValueError("Eingabe muss ein 9x9-Array sein.")
        
    lines = []
    for i in range(9):
        if i % 3 == 0 and i != 0:
            lines.append("-" * 21)

        formatted_row = []
        for j in range(0, 9, 3):
            block = " ".join(str(num) if num != 0 else '.' for num in sudoku[i, j:j+3])
            formatted_row.append(block)

        line = " | ".join(formatted_row)
        lines.append(line)

    return "\n".join(lines)
```

### Schritt 10: Verbessern der Docstrings
Aktualisieren Sie alle Docstrings, um sie vollständiger und genauer zu machen, einschließlich Rückgabetypen und Ausnahmen:

```python
def get_sudoku_string(sudoku):
    """
    Erzeugt eine lesbare Zeichenkettendarstellung eines Sudoku-Boards.
    
    Args:
        sudoku (numpy.ndarray): Ein 2D-Array, das das Sudoku-Board repräsentiert, wobei 0 eine leere Zelle darstellt.
    Returns:
        str: Eine formatierte Zeichenkette, die das Sudoku-Board darstellt.
    Raises:
        TypeError: Wenn die Eingabe kein numpy.ndarray ist.
        ValueError: Wenn die Eingabe kein 9x9-Array ist.
    """
    # ...
```

Machen Sie das Gleiche für die anderen Funktionen, um vollständige Dokumentation zu gewährleisten.

## Teil 4: Finale Anpassungen und Qualitätssicherung

### Schritt 11: Überprüfen Sie die Importe
Stellen Sie sicher, dass alle notwendigen Importe am Anfang der Datei stehen:

```python
import numpy as np
```

### Schritt 12: Konsistente Formatierung
Stellen Sie sicher, dass der Code konsistent formatiert ist (Einrückungen, Leerzeichen, etc.). Idealerweise sollten Sie einen Linter wie flake8 oder einen Formatierer wie black verwenden.

### Schritt 13: Abschließende Tests
Führen Sie Tests durch, um sicherzustellen, dass der refaktorierte Code wie erwartet funktioniert. Das Sudoku-Rätsel sollte korrekt gelöst werden und die Ausgabe sollte mit der ursprünglichen Version übereinstimmen.

## Zusammenfassung

Diese Anleitung führt durch einen systematischen Refactoring-Prozess, der den ursprünglichen Code in einen gut strukturierten, lesbaren und wartbaren Code umwandelt. Die Hauptverbesserungen umfassen:

1. Bessere Namensgebung für Variablen und Funktionen
2. Extrahieren von wiederverwendbarem Code in Funktionen
3. Verbesserte Algorithmen und Datenstrukturen
4. Hinzufügen von Fehlerbehandlung und Validierung
5. Dokumentation durch ausführliche Docstrings
6. Verbesserung der Codestruktur und -organisation

Durch das Befolgen dieser Schritte kann der Code schrittweise verbessert werden, ohne die Funktionalität zu beeinträchtigen.