
valjumine_tund = int(input("Sisesta väljumisaja tund: "))
valjumine_min = int(input("Sisesta väljumisaja minutid: "))
saabumine_tund = int(input("Sisesta saabumisaja tund: "))
saabumine_min = int(input("Sisesta saabumisaja minutid: "))

v_tund_minutiteks = valjumine_tund * 60
s_tund_minutiteks = saabumine_tund * 60

soit_kokku = (s_tund_minutiteks + saabumine_min) - (v_tund_minutiteks + valjumine_min)

soit_tunnid = soit_kokku // 60
soit_minutid = soit_kokku % 60

print("Sõit kestab kokku",soit_tunnid,"tundi ja",soit_minutid,"minutit.")