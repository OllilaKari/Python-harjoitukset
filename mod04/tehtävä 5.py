kayttajatunnus = input("kirjoita kayttajatunnuksesi:")

salasana = input("kirjoita salasanasi:")

oikea_kayttajatunnus = "kari123"

oikea_salasana = "salasana"

yritykset = 1

while (kayttajatunnus != oikea_kayttajatunnus or salasana != oikea_salasana) and yritykset < 5:
    print("väärä käyttäjätunnus tai salasana!")
    kayttajatunnus = (input("kirjoita kayttajatunnuksesi"))
    salasana = input("kirjoita salasanasi")
    yritykset = yritykset + 1


if kayttajatunnus == oikea_kayttajatunnus and salasana == oikea_salasana:
    print("Tervetuloa!")

else:
    print("pääsy evätty!")




