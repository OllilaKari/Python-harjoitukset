leiviskat = int(input("anna leiviskät:"))
naulat = int(input("anna naulat"))
luodit = int(input("anna luodit"))
luodit_yhteensa = leiviskat * 20 * 32 + luodit
grammat_yhteensa = luodit_yhteensa * 13.3
kilogrammat = int(grammat_yhteensa // 1000)
grammat = grammat_yhteensa % 1000
print("massa on", kilogrammat, "kilogrammaa ja", grammat, "grammaa.")
