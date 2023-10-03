
aasta = int(input("Sisesta aastaarv: "))

if(aasta % 4 == 0):
    if(aasta % 100 == 0 and aasta % 400 != 0):
        print("Tegu ei ole liigaastaga.")
    else:
        print("Tegu on liigaastaga.")
else:
    print("Tegu ei ole liigaastaga.")