from math import sqrt
while True:
    luku = int(input("Syötä luku: "))
    if luku == 0:
        break
    elif luku < 0:
        print("Epäkelpo luku")
    elif luku > 0:
        print(sqrt(luku))
print("Lopetetaan...")
