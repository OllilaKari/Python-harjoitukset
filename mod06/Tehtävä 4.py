def kokonaisluvut(luvut):
    yhteensa = 0

    for luku in luvut:
        yhteensa += luku
        return yhteensa
    
luvut = [5, 10, 15, 20, 25]

summa = kokonaisluvut(luvut)
print("lista", summa)
