pisteet = int(input("Anna pisteet [0-100]: "))
if 0 <= pisteet <= 49:
    print ("Arvosana: hylätty")
elif 50 <= pisteet <= 59:
    print ("Arvosana: 1")
elif 60 <= pisteet <= 69:
    print ("Arvosana: 2")
elif 70 <= pisteet <= 79:
    print ("Arvosana: 3")
elif 80 <= pisteet <= 89:
    print ("Arvosana: 4")
elif 90 <= pisteet <= 100:
    print ("Arvosana: 5")
else:
    print("Arvosana: mahdotonta!")
