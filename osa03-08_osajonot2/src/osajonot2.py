merkkijono = input("Anna merkkijono: ")
loppukohta = len(merkkijono)
alkukohta = loppukohta - 1
while alkukohta >= 0:
    print(merkkijono[alkukohta:loppukohta])
    alkukohta -= 1
