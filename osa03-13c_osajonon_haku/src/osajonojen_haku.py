sana = input("Sana: ")
merkki = input("Merkki: ")
alkuMerkki = sana.find(merkki)
if len(sana)-2 > alkuMerkki:
    print(sana[alkuMerkki:alkuMerkki+3])
