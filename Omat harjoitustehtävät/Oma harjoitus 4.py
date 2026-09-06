#lasketaan kolmion pinta ala kanta kertaa korkeus
kolmionkanta =float(input("Kerro kolmion kanta"))
#Rivillä 2 ei voinut olla sanaa kanta kahteen kertaan, muista tämä!
korkeus =float(input("kerro kolmion korkeus"))
pinta_ala = kolmionkanta * korkeus / 2
print("kolmion pinta-ala on", pinta_ala)
