def kaikki_vaarinpain(lista: list):
    returnList = []
    for i in lista[::-1]:
        returnList.append(i[::-1])
    return returnList
