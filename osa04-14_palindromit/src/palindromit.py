def palindromi(sana):
    return sana == sana[::-1]


while True:
    sana = input("Anna sana: ")
    if palindromi(sana):
        print(sana, "on palindromi!")
        break
    else:
        print("ei ollut palindromi")
