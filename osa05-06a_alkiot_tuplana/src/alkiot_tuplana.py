def tuplaa_alkiot(luvut: list):
    lista = luvut.copy()
    for i in range(len(lista)):
        lista[i] *= 2
    return lista


if __name__ == "__main__":
    luvut = [2, 4, 5, 3, 11, -4]
    tuplaluvut = tuplaa_alkiot(luvut)
    print("alkuperäinen:", luvut)
    print("tuplattu:", tuplaluvut)
