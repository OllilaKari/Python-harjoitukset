luku = (input("anna luku"))
ensimmainen = True

while luku != "":

    luku = int(luku)

    if ensimmainen:
        pienin_numero = luku
        suurin_numero = luku
        ensimmainen = False

    if luku < pienin_numero: 
        pienin_numero = luku

    if luku > suurin_numero:
        suurin_numero = luku

    luku = input("anna uusi luku")

print("pienin luku on:", pienin_numero)
print("suurin luku on:", suurin_numero)