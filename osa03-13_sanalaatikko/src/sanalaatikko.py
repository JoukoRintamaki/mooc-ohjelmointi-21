sana = input("Sana:")
tyhjienmaaraAlku = int((30-len(sana)-2)/2)
if len(sana) % 2 != 0:
    tyhjienmaaraLoppu = tyhjienmaaraAlku + 1
else:
    tyhjienmaaraLoppu = tyhjienmaaraAlku
print("*"*30)
print("*"+" "*tyhjienmaaraAlku+sana+" "*tyhjienmaaraLoppu+"*")
print("*"*30)
