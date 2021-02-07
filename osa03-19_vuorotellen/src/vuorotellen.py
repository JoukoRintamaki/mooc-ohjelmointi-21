luku = int(input("Anna luku: "))
luku1 = 1
luku2 = luku
i = 1
while i <= luku:
    if i % 2 != 0:
        print(luku1)
        luku1 += 1
    else:
        print(luku2)
        luku2 -= 1
    i += 1
