def lyhin(lista: list):
    lyhyin = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    for i in lista:
        if len(i) < len(lyhyin):
            lyhyin = i
    return lyhyin


if __name__ == "__main__":
    lista = ["eka", "toka", "kolmas", "seitsemäs"]

    tulos = lyhin(lista)
    print(tulos)
    lista = ["pekka", "emilia", "johanna", "venla", "eero", "antti"]

    tulos = lyhin(lista)
    print(tulos)
