import math

kaatet1 = float(input("Sisesta esimese kaateti pikkus: "))
kaatet2 = float(input("Sisesta teise kaateti pikkus: "))

hypotenuus = math.sqrt(kaatet1**2 + kaatet2**2)

pindala = (kaatet1 * kaatet2) / 2

ymbermoot = kaatet1 + kaatet2 + hypotenuus


print("Kolmnurga pindala on ", pindala, " ja ümbermõõt on ", round(ymbermoot, 1))