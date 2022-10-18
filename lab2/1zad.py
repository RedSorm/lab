x = input("wprowadz wiek: ")
x = int(x)
if x < 4:
    cena = 0
elif 4 <= x <= 18:
    cena = 10
else:
    cena = 20
print(f"cena biletu: {cena} zł")



