def lue_hedelmat():
    hedelmat = {}
    with open("hedelmat.csv") as tiedosto:
        for rivi in tiedosto:
            hedelmat[rivi.split(";")[0]] = float(rivi.split(";")[1])
    return hedelmat


if __name__ == "__main__":
    print(lue_hedelmat())
