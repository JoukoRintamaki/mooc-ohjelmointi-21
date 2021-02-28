def transponoi(matriisi: list):
    transponointuMatriisi = []
    for sarake in range(len(matriisi)):
        riviLisattava = []
        for rivi in range(len(matriisi[sarake])):
            riviLisattava.append(matriisi[rivi][sarake])
        transponointuMatriisi.append(riviLisattava)
    for i in range(len(matriisi)):
        matriisi[i] = transponointuMatriisi[i]


if __name__ == "__main__":
    matriisi = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    transponoi(matriisi)
    print(matriisi)
