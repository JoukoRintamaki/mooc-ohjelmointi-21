import math
opiskelijoita = int(input("Montako opiskelijaa? "))
ryhmanKoko = int(input("Mikä on ryhmän koko? "))
print(f"Ryhmien määrä: {math.ceil(opiskelijoita/ryhmanKoko)}")