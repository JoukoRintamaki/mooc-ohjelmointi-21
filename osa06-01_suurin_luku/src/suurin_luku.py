def suurin():
    luvut = []
    with open("luvut.txt") as tiedosto:
        for rivi in tiedosto:
            luvut.append(int(rivi))
    return max(luvut)


if __name__ == "__main__":
    print(suurin())
