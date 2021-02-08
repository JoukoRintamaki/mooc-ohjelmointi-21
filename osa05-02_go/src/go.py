def kumpi_voitti(pelilauta: list):
    ykkostenMaara = 0
    kakkostenMaara = 0
    for i in pelilauta:
        for j in i:
            if j == 1:
                ykkostenMaara += 1
            elif j == 2:
                kakkostenMaara += 1
    if ykkostenMaara > kakkostenMaara:
        return 1
    elif ykkostenMaara < kakkostenMaara:
        return 2
    else:
        return 0