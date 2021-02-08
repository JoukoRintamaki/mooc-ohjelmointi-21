def pisin(sanaLista):
    pisinSana = ""
    for sana in sanaLista:
        print (len(sana),len(pisinSana))
        if len(sana) > len(pisinSana):
            pisinSana = sana
    return pisinSana


if __name__ == "__main__":
    jonot = ["moi", "moikka", "heip", "hellurei", "terve"]
    print(pisin(jonot))
