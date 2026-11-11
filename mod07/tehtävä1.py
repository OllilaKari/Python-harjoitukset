 
vuodenajat = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")

kuukausi = int(input("Anna jonkun kuukauden numero (1-12)"))

if 1 <= kuukausi <= 12:
    vuodenaika = vuodenajat [kuukausi - 1]
    print("vuoden aika on", vuodenaika)
else:
    print ("Tälläistä kuukautta ei ole olemassa!")
               
