import random

def heita_noppaa (tahkot):

    return random.randint(1, tahkot)

maksimi = int(input("Anna nopan tahkojen määrä"))

while True:
    silmaluku = heita_noppaa(maksimi)
    print("Nopan silmäluku:", silmaluku)
    if silmaluku == maksimi:
        break