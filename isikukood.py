import time

isikukood = "49210030250"
    
if int(isikukood[0]) % 2 == 0:
    print("Tegu on naisterahvaga.")
else:
    print("Tegu on meesterahvaga.")
    
kuu = isikukood[3:5]
paev = isikukood[5:7]
aasta = isikukood[1:3]

if(isikukood[0] == '1' or isikukood[0] == '2'):
    taisaasta = '18' + aasta
elif(isikukood[0] == '3' or isikukood[0] == '4'):
    taisaasta = '19' + aasta
elif(isikukood[0] == '5' or isikukood[0] == '6'):
    taisaasta = '20' + aasta

aeg = time.localtime()

vanus = aeg.tm_year - int(taisaasta)
if(aeg.tm_mon < int(kuu)):
    vanus = vanus - 1
elif(aeg.tm_mon == int(kuu)):
    if(aeg.tm_mday <= int(paev)):
        vanus = vanus - 1

print("Isiku sünnipäev on",paev+"."+kuu)
print(taisaasta)
print(vanus)