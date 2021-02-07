asti = int(input("Mihin asti: "))
luku = 1
summa = 1
laskettiin = f"Laskettiin {luku}"
while summa < asti:    
    laskettiin += f" + "
    luku += 1
    summa += luku
    laskettiin += f"{luku}"
laskettiin += f" = {summa}"
print(laskettiin)
