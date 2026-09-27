import random

luku = random.randint(1,10)

kysymys =int(input("anna luku väliltä 1-10"))

while kysymys != luku:
    if kysymys < luku:
        print("liian pieni arvaus")

    if kysymys > luku:
        print("liian suuri arvaus")

    kysymys =int(input("Arvaa uudelleen"))

print("oikein!")
