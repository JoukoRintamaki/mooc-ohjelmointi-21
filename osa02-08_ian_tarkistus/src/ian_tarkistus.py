age = int(input("Kerro ikäsi? "))
if (age < 0):
    print("Taitaa olla virhe")
elif (0 <= age < 5):
    print("En usko, että osaat kirjoittaa...")
else:
    print(f"Ok, olet siis {age}-vuotias")
