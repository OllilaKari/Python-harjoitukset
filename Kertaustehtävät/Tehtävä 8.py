kustannukset = [12,7,6,2,10]

yhteensa = 0

for kustannus in kustannukset:
    print("tuotteen valmistamiskustannus", kustannus, "€")
    yhteensa += kustannus

print("valmistamiskustannukset yhteensa", yhteensa, "€")
