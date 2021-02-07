luku = int(input("Luku: "))
if (luku % 5) == 0 and (luku % 3) == 0:
    tuloste = "FizzBuzz"
elif (luku % 5) == 0:
    tuloste = "Buzz"
elif (luku % 3) == 0:
    tuloste = "Fizz"
print(tuloste)
