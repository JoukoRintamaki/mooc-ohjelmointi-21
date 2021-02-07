def viiva(koko, merkki):
    if merkki == "":
        merkki = "*"
    print(merkki[0] * koko)


def risunelio(koko):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    rivi = koko
    while rivi > 0:
        viiva(koko, "#")
        rivi -= 1


# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risunelio(5)
