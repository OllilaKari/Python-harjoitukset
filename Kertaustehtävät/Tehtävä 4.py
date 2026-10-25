from math import sqrt
while True:
    kokonaisluku = int(input("Anna joku kokonaisluku"))

    if kokonaisluku < 0:
        print("virheellinen numero!")

    if kokonaisluku > 0:
        neliojuuri = sqrt(kokonaisluku)
        print("luvun neliojuuri on", neliojuuri)
    if kokonaisluku == 0:
        break
    
