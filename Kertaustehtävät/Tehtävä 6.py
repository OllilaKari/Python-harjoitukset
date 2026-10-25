luvut = []

while True:
    luku = int(input("anna joku luku"))

    if luku == 0:
        break
    luvut.append(luku)
    print(luvut)
    
    jarjestetyt = luvut.copy()

    jarjestetyt.sort()
    print(jarjestetyt)



