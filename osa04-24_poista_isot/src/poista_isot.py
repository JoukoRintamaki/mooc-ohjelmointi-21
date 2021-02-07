def poista_isot(lista):
    return list(filter(lambda x: x.isupper() == False, lista))