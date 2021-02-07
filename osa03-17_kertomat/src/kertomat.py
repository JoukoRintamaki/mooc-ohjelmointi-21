while True:
    luku = int(input("Anna luku: "))
    if not luku <= 0:
        
        kertoma = 1
        i = 1
        while i <= luku:
            kertoma = kertoma * i
            i += 1
        print(f"Luvun {luku} kertoma on {kertoma}")
    else:
        break
print("Kiitos ja moi!")
