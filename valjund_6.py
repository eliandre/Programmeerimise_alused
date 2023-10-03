# muutujale antakse ujukoma väärtus, seejärel trükitakse see välja
# täpsusega kolm kohta peale koma

arv = 13.45685343634636

# Nn new-style formatting kasutades stringi meetodit format()
print("Arv {0} on kolme komakohani ümardatult {0:0.3f}.".format(arv))

# Veel üks võimalus stringi formaatimiseks
print(f"Arv {arv} on kolme komakohani ümardatult {arv:0.3f}.")

# Ja nn old-style formatting
print("Arv %f on kolme komakohani ümardatult %0.3f." % (arv,arv))

