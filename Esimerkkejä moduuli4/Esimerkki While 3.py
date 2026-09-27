print("-----Tervetuloa laskinohjelmaan------")

print("Valitse mitä toimintoa haluat käyttää")

print("A: yhteenlasku, B: Vähennyslasku, C: Kertolasku, D: Jakolasku")
valinta = input("Anna valintasi").upper()

a = float(input("anna ensimmäinen luku"))
b = float(input("anna toinen luku:"))


if valinta == "A":
    print(f"Lukujen {a} ja {b} summa on {a+b}")
    
elif valinta =="B":
        print(f"lukujen {a} ja {b} erotus on {a-b}.")
        
elif valinta =="C":
      print(f"lukujen {a} ja {b} tulo on {a*b}")
      
elif valinta == "D":
    print(f("lukujen {a} ja {b} osamäärä on {a/b}"))
elif valinta == "Q":
     print("poistutaan...")
     

else:
    print("Valintasi on virheellinen!")




