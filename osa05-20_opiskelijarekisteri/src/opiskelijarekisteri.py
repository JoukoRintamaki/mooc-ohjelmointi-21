from typing import NoReturn


def lisaa_opiskelija(opiskelijat: dict, nimi: str):
    suoritukset = {}
    opiskelijat[(nimi)] = suoritukset


def tulosta(opiskelijat: dict, nimi: str):
    if nimi in opiskelijat:
        print(nimi, ":", sep="")
        if len(opiskelijat[nimi]) == 0:
            print(" ei suorituksia")
        else:
            print(" suorituksia", len(opiskelijat[nimi]), "kurssilta:")
            suoritustenSumma = 0
            for suorituksenNimi, suoritus in opiskelijat[nimi].items():
                print(" ", suorituksenNimi, suoritus)
                suoritustenSumma += suoritus
            print(" keskiarvo", suoritustenSumma/len(opiskelijat[nimi]))
    else:
        print("ei löytynyt ketään nimellä", nimi)


def lisaa_suoritus(opiskelijat: dict, nimi: str, suoritus: tuple):
    if suoritus[1] != 0:
        if suoritus[0] in opiskelijat[nimi]:
            if opiskelijat[nimi][suoritus[0]] < suoritus[1]:
                opiskelijat[nimi][suoritus[0]] = suoritus[1]
        else:
            opiskelijat[nimi][suoritus[0]] = suoritus[1]


def kooste(opiskelijat: dict):
    print("opiskelijoita", len(opiskelijat))
    enitenSuorituksiaNimi = ""
    isoinsuoritustenMaara = 0
    paraskeskiarvoNimi = ""
    paraskeskiArvo = 0
    for nimi, suoritukset in opiskelijat.items():
        if len(suoritukset) > isoinsuoritustenMaara:
            enitenSuorituksiaNimi = nimi
            isoinsuoritustenMaara = len(suoritukset)
        suoritustenSumma = 0
        for suorituksenNimi, suoritus in opiskelijat[nimi].items():
            suoritustenSumma += suoritus
        if suoritustenSumma/len(opiskelijat[nimi]) > paraskeskiArvo:
            paraskeskiarvoNimi = nimi
            paraskeskiArvo = suoritustenSumma/len(opiskelijat[nimi])
    print("eniten suorituksia", isoinsuoritustenMaara, enitenSuorituksiaNimi)
    print("paras keskiarvo", paraskeskiArvo, paraskeskiarvoNimi)


if __name__ == "__main__":
    opiskelijat = {}
    lisaa_opiskelija(opiskelijat, "Pekka")
    lisaa_opiskelija(opiskelijat, "Liisa")
    lisaa_suoritus(opiskelijat, "Pekka", ("Lama", 1))
    lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 1))
    lisaa_suoritus(opiskelijat, "Pekka", ("Tira", 1))
    lisaa_suoritus(opiskelijat, "Liisa", ("Ohpe", 5))
    lisaa_suoritus(opiskelijat, "Liisa", ("Jtkt", 4))
    kooste(opiskelijat)
