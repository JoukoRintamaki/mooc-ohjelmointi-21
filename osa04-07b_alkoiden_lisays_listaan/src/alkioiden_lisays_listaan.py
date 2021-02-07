lista = []
lukujenMaara = int(input("Kuinka monta lukua: "))
i=1
while lukujenMaara > 0:
    lista.append(int(input(f"Anna luku {i}:")))
    i += 1
    lukujenMaara -= 1
print (lista)
