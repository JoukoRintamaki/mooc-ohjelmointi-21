def viiva(koko, merkki):
    if merkki == "":
        merkki = "*"
    print(merkki[0] * koko)


def nelio(leveys, rivi, merkki):
    i = 0
    while i < rivi:
        viiva(leveys, merkki)
        i += 1


def kolmio(koko, merkki):
    i = 0
    while i < koko:
        i += 1
        viiva(i, merkki[0])


def kuvio(koko1, merkki1, koko2, merkki2):
    kolmio(koko1, merkki1)
    nelio(koko1, koko2, merkki2)


if __name__ == "__main__":
    kuvio(5, "x", 2, "o")
