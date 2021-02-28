def vanhin(henkilot: list):
    vanhin=""
    vanhinIka=2999
    for henkilo in henkilot:
        if henkilo[1] <  vanhinIka:
            vanhin=henkilo[0]
            vanhinIka=henkilo[1]
    return vanhin

if __name__ == "__main__":
    h1 = ("Arto", 1977)
    h2 = ("Einari", 1985)
    h3 = ("Maija", 1953)
    h4 = ("Essi", 1997)
    hlista = [h1, h2, h3, h4]

    print(vanhin(hlista))
