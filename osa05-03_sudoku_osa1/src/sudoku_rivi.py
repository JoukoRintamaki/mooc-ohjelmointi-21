def rivi_oikein(sudoku: list, rivi_nro: int):
    for i in range(1, 10):
        if sudoku[rivi_nro].count(i) > 1:
            return False
    return True
