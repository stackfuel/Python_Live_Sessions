// Statisch typisierte Sprache - Java

public class Main {
    public static void main(String[] args) {
        // Deklaration und Initialisierung eines Integers
        int variable = 10;
        System.out.println(variable);  // Ausgabe: 10

        // Versuch, einen String zur selben Variablen zuzuweisen
        // (wird Kompilierungsfehler verursachen)
        variable = "Hallo, Welt!";
        // Fehler: Inkompatible Typen: String kann nicht in int konvertiert werden

        // Deklaration und Initialisierung eines Strings
        String text = "Hallo, Welt!";
        System.out.println(text);  // Ausgabe: Hallo, Welt!
    }
}


