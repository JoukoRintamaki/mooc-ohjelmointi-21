def sarake_oikein(sudoku: list, sarake_nro: int):
    sarake = []
    for rivi in sudoku:
        sarake.append(rivi[sarake_nro])
    for i in range(1, 10):
        if sarake.count(i) > 1:
            return False
    return True
