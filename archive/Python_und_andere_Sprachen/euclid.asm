section .data
    ; Hier können wir die Zahlen definieren, für die wir den GGT berechnen möchten
    num1 db 56   ; erste Zahl
    num2 db 98   ; zweite Zahl

section .bss
    result resb 1  ; Speicher für das Ergebnis

section .text
    global _start

_start:
    ; Lade die beiden Zahlen in Register
    mov al, [num1]
    mov bl, [num2]

euclidean_algorithm:
    ; Prüfe, ob bl gleich 0 ist
    cmp bl, 0
    je done

    ; Berechne den Rest von al / bl und speichere ihn in ah
    xor ah, ah    ; Setze ah auf 0
    div bl        ; Dividiere al durch bl, Rest ist in ah

    ; Verschiebe bl nach al und den Rest (ah) nach bl
    mov al, bl
    mov bl, ah

    ; Wiederhole den Algorithmus
    jmp euclidean_algorithm

done:
    ; Speichere das Ergebnis in der result-Variable
    mov [result], al

    ; Beende das Programm
    mov eax, 60   ; syscall: exit
    xor edi, edi  ; exit code 0
    syscall
