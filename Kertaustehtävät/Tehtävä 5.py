tarina = []

while True:
    sana = input("Aloita tarinasi ja kerro joku sana")
    if sana == "loppu":
        break
    tarina.append(sana)

for sana in tarina:
    print(sana, end=" ")
    


