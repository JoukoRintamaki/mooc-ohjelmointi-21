from math import sqrt
a = float(input("Anna a: "))
b = float(input("Anna b: "))
c = float(input("Anna c: "))

juuri1 = (-b + sqrt(b**2-4*a*c))/(2*a)
juuri2 = (-b - sqrt(b**2-4*a*c))/(2*a)

print(f"Juuret ovat {juuri1} ja {juuri2}")
