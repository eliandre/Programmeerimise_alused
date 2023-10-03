
arv1 = float(input("Sisesta esimene arv: "))
arv2 = float(input("Sisesta Teine arv: "))

if arv2 == 0:
    print("Nulliga jagada ei saa!")
else:
    tulemus = arv1 /arv2
    print(round(tulemus,2))