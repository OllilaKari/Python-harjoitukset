hyttiluokka = input(("kerro minkä luokan hytin olet valinnut, hyttiluokat ovat seuraavat: Lux,A,B,C?"))
if hyttiluokka == "lux":
    print("LUX on parvekkeellinen  hytti yläkannella")


elif hyttiluokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella")

elif hyttiluokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella")

elif hyttiluokka == "C":
    print("C on ikkunaton hyttti autokannen alapuolella")

else:
    print("Virheellinen hyttiluokka!")
