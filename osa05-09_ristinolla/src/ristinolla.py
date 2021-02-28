def pelaa_siirto(lauta: list, x: int, y: int, nappula: str):
    if (x in (0, 1, 2) and y in (0, 1, 2)):
        if lauta[y][x] == "":
            lauta[y][x] = nappula
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    lauta = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(pelaa_siirto(lauta, 2, 0, "X"))
    print(lauta)
