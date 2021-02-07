pisteet = int(input("Kuinka paljon pisteitä? "))
pisteetLaskettu = 0
if pisteet < 100:
    pisteetLaskettu = 1.1 * pisteet
    prosentti = 10
if pisteet >= 100:
    pisteetLaskettu = 1.15 * pisteet
    prosentti = 15
print(f"Sait {prosentti} % bonusta")
print(f"Pisteitä on nyt {pisteetLaskettu}")
