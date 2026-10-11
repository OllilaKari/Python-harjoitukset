luvut = []

while True:
    syote = input("anna luku")
    if syote == "":
        break
    luvut.append(float(syote))


luvut.sort(reverse=True)

for luku in luvut[:5]:
    print(luku)
