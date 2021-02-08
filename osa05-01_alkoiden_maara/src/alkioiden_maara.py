def laske_alkiot(matriisi: list, alkio: int):
    alkioidenMaara = 0
    for rivi in matriisi:
        for sarake in rivi:
            if sarake == alkio:
                alkioidenMaara += 1
    return alkioidenMaara