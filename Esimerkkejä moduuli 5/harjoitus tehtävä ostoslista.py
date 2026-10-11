#luo ostoslista tuotteista. Tee while silmukka jossa kysyt käyttäjältä tuotetta syötteenä. Ohjelman pitää poistaa tuotteet yksi kerrallaan listasta ja tulostaa jäljellä olevat tuotteet jokaisen ostoksen jälkeen. Jos tuotetta ei ole listalla, ilmoita siitä 

ostoslista = ["maito", "rahka", "juusto", "leipä", "kahvi"]

while ostoslista:
    tuote = input("minkä tuotteen ostit?")
    #käytännössä tarkoittaa, että while toistaa tätä niin kauan kun ostoslista ei ole tyhjä

    if tuote in ostoslista:
        ostoslista.remove(tuote)
        print("jäljellä olevat tuotteet", ostoslista)

    else:
        print("tuotetta ei ole listalla!")
