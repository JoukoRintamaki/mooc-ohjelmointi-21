def pisimman_pituus(lista: list):
    paras = 0
    for i in lista:
        if len(i) > paras:
            paras = len(i)
    return paras
