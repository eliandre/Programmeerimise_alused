
pikkus = float(input("Sisesta põranda pikkus: "))
laius = float(input("Sisesta põranda laius: "))
varvikulu = float(input("Sisesta värvikulu ruutmeetri kohta: "))

pindala = pikkus * laius


print("Värvi kulub", pindala * varvikulu, "liitrit.")