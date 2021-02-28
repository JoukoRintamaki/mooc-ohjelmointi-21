def hae(puhelinluettelo: dict):
    nimi = input("nimi: ")
    if nimi in puhelinluettelo:
        for numero in puhelinluettelo[nimi]:
            print (numero)
    else:
        print("ei numeroa")


def lisaa(puhelinluettelo: dict):
    nimi = input("nimi: ")
    numero = input("numero: ")
    numerot = []
    if nimi in puhelinluettelo:
        numerot = puhelinluettelo[nimi]
    numerot.append(numero)
    puhelinluettelo[nimi] = numerot
    print("ok!")


puhelinluettelo = {}
while True:
    komento = input("komento (1 hae, 2 lisää, 3 lopeta): ")
    if komento == "3":
        print("lopetetaan...")
        break
    elif komento == "1":
        hae(puhelinluettelo)
    elif komento == "2":
        lisaa(puhelinluettelo)
