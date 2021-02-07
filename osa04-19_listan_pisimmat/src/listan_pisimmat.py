def pisimmat(lista: list):
    pisimmat = []
    pisimmat.append(lista[0])
    for i in lista:
        if len(i) > len(pisimmat[0]):
            pisimmat.clear()
            pisimmat.append(i)
        elif len(i) == len(pisimmat[0]) and i not in pisimmat:
            pisimmat.append(i)
    return pisimmat


if __name__ == "__main__":
    lista = ["eka", "toka", "kolmas", "seitsemäs"]
    tulos = pisimmat(lista)
    print(tulos)  # ['seitsemäs']
    lista = ["pekka", "emilia", "venla", "eero", "antti", "juhani"]
    tulos = pisimmat(lista)
    print(tulos)  # ['emilia', 'juhani']
