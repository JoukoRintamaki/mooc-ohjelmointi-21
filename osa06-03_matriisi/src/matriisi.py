def lueMatriisi():
    matriisi = []
    with open("matriisi.txt") as tiedosto:
        for rivi in tiedosto:
            matriisi.append(list(map(int, rivi.split(","))))
    return matriisi


def to1dList():
    return [j for sub in lueMatriisi() for j in sub]


def summa():
    return sum(to1dList())


def maksimi():
    return max(to1dList())


def rivisummat():
    riviSummat = []
    for rivi in lueMatriisi():
        riviSummat.append(sum(rivi))
    return riviSummat


if __name__ == "__main__":
    print(rivisummat())
