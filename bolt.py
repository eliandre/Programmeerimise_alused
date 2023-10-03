
minutihind = float(input("Sisesta minutihind: "))
max_tunnihind = float(input("Sisesta maksimaalne tunnihind: "))
max_paevahind = float(input("Sisesta maksimaalne päevahind: "))
km_hind = float(input("Sisesta kilomeetrihind: "))
labitud_km = float(input("Sisesta läbitud kilomeetrite arv: "))
aeg_t = float(input("Sisesta sõidetud tunnid: "))
aeg_m = float(input("Sisesta sõidetud minutit: "))

aeg_minutites = int(aeg_t * 60 + aeg_m)

if(aeg_minutites < 59):
    if((minutihind * aeg_m) > max_tunnihind):
        hind = max_tunnihind + km_hind * labitud_km
    else:
        hind = minutihind * aeg_m + km_hind * labitud_km
elif(60 <= aeg_minutites < 1439):
    if((max_tunnihind * aeg_t > max_paevahind)):
        hind = max_paevahind + (km_hind * labitud_km)
    else:
        hind = (max_tunnihind * aeg_t) + (aeg_m * minutihind) + (km_hind * labitud_km)
else:
    paevad = aeg_t // 24
    tunnid_ule = aeg_t % 24
    if((tunnid_ule * max_tunnihind) > max_paevahind):
        hind = max_paevahind * paevad + tunnid_ule * max_tunnihind + aeg_m * minutihind + km_hind * labitud_km
    else:
        hind = max_paevahind * paevad + tunnid_ule * max_tunnihind + aeg_m * minutihind + km_hind * labitud_km
    print(max_paevahind * paevad)
    print(tunnid_ule * max_tunnihind)
    print(aeg_m * minutihind)
    print(km_hind * labitud_km)

print("Sõidu hind on kokku",round(hind, 2),"€.")