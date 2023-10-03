import math

a = float(input("Sisesta esimene arv: "))
b = float(input("Sisesta teine arv: "))
c = float(input("Sisesta kolmas arv: "))

if(a == 0) or (b == 0):
    print("Tegu pole ruutvõrrandiga!")
elif(b * b - 4 * a * c) < 0:
    print("Võrrandil pole reaalarvulisi lahendeid.")
else:
    x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)

    print("Ruutvõrrandi lahendid on: x1 = "+str(x1)+", x2 = "+str(x2))