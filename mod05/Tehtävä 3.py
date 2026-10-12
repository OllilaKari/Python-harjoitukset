luku = int(input("Anna joku kokonaisluku"))

on_alkuluku= luku >1

for jakaja in range(2, luku):

    if luku % jakaja == 0:
        on_alkuluku = False
    break

if on_alkuluku:
    print ("luku on alkuluku")
else:
    print("luku ei ole alkuluku")
