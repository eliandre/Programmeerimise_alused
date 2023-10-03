
kulg1 = int(input("Sisesta esimese külje pikkus: "))
kulg2 = int(input("Sisesta teise külje pikkus: "))
kulg3 = int(input("Sisesta kolmanda külje pikkus: "))

if(kulg1 + kulg2) > kulg3:
    if(kulg2 + kulg3) > kulg1:
        if(kulg1 + kulg3) > kulg2:
            if(kulg1 == kulg2) and (kulg2 == kulg3) and (kulg1 == kulg3):
                print("Tegu on võrdkülgse kolmnurgaga.")
            elif(kulg1 == kulg2) or (kulg2 == kulg3) or (kulg1 == kulg3):
                print("Tegu on võrdhaarse kolmnurgaga.")
            else:
                print("Tegu on erikülgse kolmnurgaga.")
else:
    print("Antud küljepikkustega ei saa moodustada kolmnurka.")