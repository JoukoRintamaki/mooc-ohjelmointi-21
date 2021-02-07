def uniikit(lista: list):
    listaUniikit = []
    for i in lista:
        if i not in listaUniikit:
            listaUniikit.append(i)
    return sorted(listaUniikit)


if __name__ == "__main__":
    lista = [3, 2, 2, 1, 3, 3, 1]
    print(uniikit(lista))  # [1, 2, 3]
