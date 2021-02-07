def pisin_naapurijono(lista: list):
    laskuri = 1
    pituus = 0
    for i in range(len(lista)):
        if i < (len(lista)-1):
            if (abs(lista[i] - lista[i+1])) == 1:
                laskuri += 1
                if laskuri > pituus:
                    pituus = laskuri
            else:
                laskuri = 1
    return pituus