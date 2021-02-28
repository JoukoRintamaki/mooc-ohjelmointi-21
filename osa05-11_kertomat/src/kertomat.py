def kertomat(n: int):
    kertomatDictionary = {}
    i = 1
    while i <= n:
        j = i
        lukuKertoma = 1
        while j > 0:
            lukuKertoma *= j
            j -= 1
        kertomatDictionary[i] = lukuKertoma
        i += 1
    return kertomatDictionary