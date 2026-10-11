#luo ohjelma joka kysyy käyttäjältä hänen lempivärinsä, tarkista löytyykö lempiväri ennalta määritellystä värilistasta ja vastaa sen mukaisesti. Määrittele lista itse

varit = ["sininen", "vihrea", "musta", "punainen"]

lempivari = input("mikä on lempivärisi")

if lempivari in varit:
    print("lempivärisi on listalla!")

else:
    print("lempiväriäsi ei ole listalla!")