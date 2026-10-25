tuotteet = []
maarat = []

while True:
    tuote = input("Mitä tuotetta valmistetaan? ")
    maara = int(input("Kuinka monta valmistetaan? "))

    tuotteet.append(tuote)
    maarat.append(maara)

    jatketaanko = input("Jatketaanko tuotantoa? ")

    if jatketaanko == "Ei":
        break

print("Tuotanto lopetettu!")
print("Valmistetut tuotteet:")
