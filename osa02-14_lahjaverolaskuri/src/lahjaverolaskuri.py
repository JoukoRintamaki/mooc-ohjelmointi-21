lahja = int(input("Lahjan suuruus? "))
if lahja < 5000:
    print("Ei veroa")
else:
    if 5000 <= lahja < 25000:
        vero = 100+(lahja - 5000)*0.08
    elif 25000 <= lahja < 55000:
        vero = 1700+(lahja - 25000)*0.1
    elif 55000 <= lahja < 200000:
        vero = 4700+(lahja - 55000)*0.12
    elif 200000 <= lahja < 1000000:
        vero = 22100+(lahja - 200000)*0.15
    elif 1000000 <= lahja:
        vero = 142100+(lahja - 1000000)*0.17
    print(f"Vero: {vero} euroa")
