def tulosta(sudoku: list):
    i = 1
    for rivi in sudoku:
        for x in range(0, 9, 3):
            for y in range(0, 3):
                if rivi[x+y] == 0:
                    print("_ ", end="")
                else:
                    print(rivi[x+y],"", end="")
            if (x != 6):
                print(" ", end="")
            else:
                print()
        if i in (3, 6):
            print()
        i += 1
    return sudoku


def lisays(sudoku: list, rivi_nro: int, sarake_nro: int, luku: int):
    sudoku[rivi_nro][sarake_nro] = luku
    return sudoku


if __name__ == "__main__":
    sudoku = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    tulosta(sudoku)
    lisays(sudoku, 0, 0, 2)
    lisays(sudoku, 1, 2, 7)
    lisays(sudoku, 5, 7, 3)
    print()
    print("Kolme numeroa lisätty:")
    print()
    tulosta(sudoku)
