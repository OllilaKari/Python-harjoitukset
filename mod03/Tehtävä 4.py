vuosiluku = int(input("kerro mikä vuosiluku nyt on?"))
if vuosiluku % 4 == 0:
    print("tänä vuonna on karkausvuosi")

elif vuosiluku % 100 == 0:
    print("Vuosi ei ole karkausvuosi")