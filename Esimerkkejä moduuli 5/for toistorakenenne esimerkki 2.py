nimet = []

#pelkät hakasulkeet = tyhjälista

nimi =input("anna joku nimi")

while nimi != "":

#while looppi tarkoittaa kunhan lista ei ole tyhjä
    nimet.append(nimi)
    nimi = input("anna joku nimi")

for n in nimet:
    print(f"Tervehdys {n}!")