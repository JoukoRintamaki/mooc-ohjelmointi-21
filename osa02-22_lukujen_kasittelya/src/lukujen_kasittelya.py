print("Syötä kokonaislukuja, 0 lopettaa:")
lukumaara = 0
summa = 0
positiiviset = 0
negatiiviset = 0
while True:
    luku = int(input("Luku: "))
    if luku == 0:
        break
    lukumaara += 1
    summa += luku
    if luku < 0:
        negatiiviset += 1
    else:
        positiiviset += 1
print(f"Lukuja yhteensä {lukumaara}")
print(f"Lukujen summa {summa}")
print(f"Lukujen keskiarvo {summa/lukumaara}")
print(f"Positiivisia {positiiviset}")
print(f"Negatiivisia {negatiiviset}")
