def shakkilauta(a):
    i = a
    ekaMerkki = True
    while i > 0:
        j = a
        merkki = ekaMerkki
        while j > 0:
            print(int(merkki), end='')
            merkki = not merkki
            j -= 1
        print()
        i -= 1
        ekaMerkki = not ekaMerkki


if __name__ == "__main__":
    shakkilauta(3)
