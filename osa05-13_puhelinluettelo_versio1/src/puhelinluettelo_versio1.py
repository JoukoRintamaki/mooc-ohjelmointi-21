def hae(puhelinluettelo: dict):
    nimi = input("nimi: ")
    if nimi in puhelinluettelo:
        print(puhelinluettelo[nimi])
    else:
        print("ei numeroa")


def lisaa(puhelinluettelo: dict):
    nimi = input("nimi: ")
    numero = input("numero: ")
    puhelinluettelo[nimi] = numero
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
