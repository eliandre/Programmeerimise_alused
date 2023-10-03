
kodu_kaugus = int(input("Sisesta jalgratturi kaugus kodust (km): "))
jalgratturi_kiirus = int(input("Sisesta jalgratturi kiirus (km/h): "))
karbse_kiirus = int(input("Sisesta kärbse kiirus (km/h): "))

ratturi_aeg = kodu_kaugus / jalgratturi_kiirus
karbse_vahemaa = ratturi_aeg * karbse_kiirus

print("Kärbes lendas kokku",round(karbse_vahemaa, 2),"km.")