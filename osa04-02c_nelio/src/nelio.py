def viiva(koko, merkki):
    if merkki == "":
        merkki = "*"
    print(merkki[0] * koko)


def nelio(koko, merkki):
    rivi = koko
    while rivi > 0:
        viiva(koko, merkki)
        rivi -= 1


# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    nelio(5, "x")
