import random
arpakuutiot = int(input("Kerro arpakuutioiden lukumäärä"))

summa = 0

for a in range(arpakuutiot):
    silmaluku = random.randint (1,6)
    print(silmaluku)
    summa = summa + silmaluku

print("arpakuutoiden lukujen summa on", summa)

