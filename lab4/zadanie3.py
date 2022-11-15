zwierzeta = []
y = 0
while y < 4:
    x = input("Podaj nazwy zwierząt: ")
    zwierzeta.append(x)
    y += 1
print(zwierzeta)
a =sorted(zwierzeta)
print(a)
print(zwierzeta[0])
print(zwierzeta[-1])
print(zwierzeta[-2])
print(zwierzeta[-3])
print(zwierzeta.sort())
print(len(zwierzeta))
