def eniten_kirjainta(merkkijono: str):
    isoinluku = 0
    for i in merkkijono:
        if merkkijono.count(i) > isoinluku:
            isoinluku = merkkijono.count(i)
            palautettavaMerkki = i
    return palautettavaMerkki
