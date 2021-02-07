def viiva(koko, merkki):
    if merkki == "":
        merkki = "*"
    print(merkki[0] * koko)


def kolmio(koko):
    i = 1
    while koko > 0:
        viiva(i, "#")
        koko -= 1
        i += 1


# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    kolmio(5)
