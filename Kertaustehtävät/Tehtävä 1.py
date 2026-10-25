tuntipalkka = float(input("Kerro tuntipalkkasi"))

#Kysyy tuntipalkan float, koska desimaalit

tunnit = float(input("kerro tehdyt työtunnit"))

päivä = input("Kerro viikonpäivä")

if päivä == "sunnuntai":
    päiväpalkka = tuntipalkka * 2 * tunnit
else:
    päiväpalkka = tuntipalkka * tunnit

print ("sinulle on kertynyt töitä", tunnit, "sinun tuntipalkallasi", tuntipalkka, "tällä viikonpäivällä", päivä)

print ("päiväpalkkasi on", päiväpalkka)


