unicafe = int(input("Montako kertaa viikossa syöt Unicafessa? "))
unicafe *= float(input("Unicafe-lounaan hinta? "))
rahaaRuokaostoksiin = float(input("Paljonko käytät viikossa ruokaostoksiin? "))

print("Kustannukset keskimäärin:")
print(f"Päivässä {(unicafe+rahaaRuokaostoksiin)/7} euroa")
print(f"Viikossa {unicafe+rahaaRuokaostoksiin} euroa")
