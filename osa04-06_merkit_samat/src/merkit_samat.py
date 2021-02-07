def samat(sana, indeksi1, indeksi2):    
    if (0 <= indeksi1 < len(sana)) and (0 <= indeksi2 < len(sana)):
        return sana[indeksi1] == sana[indeksi2]
    else:
        return False


if __name__ == "__main__":
    print(samat("ohjelmointi", 6, 0))