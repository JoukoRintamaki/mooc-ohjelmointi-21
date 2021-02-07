yritystä = 0
pin = "4321"
while True:
    yritystä += 1
    if input("PIN koodi: ") == pin:
        break
    print("Väärin")
if yritystä == 1:
    print("Oikein, tarvitsit vain yhden yrityksen!")
else:
    print(f"Oikein, tarvitsit {yritystä} yritystä")
