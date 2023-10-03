
eesti_keel = int(input("Sisesta eesti keele riigieksami punktid: "))
test = int(input("Sisesta testi eest saadud punktid: "))
lavend = int(input("Sisesta lävend: "))

e_protsent = eesti_keel * 0.25
t_protsent = test * 0.75

kokku_hetkel = e_protsent + t_protsent

vestlus = (lavend - kokku_hetkel) / 0.75

print("Vestluselt on vaja saada",round(vestlus,2),"punkti.")