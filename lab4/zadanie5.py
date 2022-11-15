import random
# punkty=[]
# for i in range(15):
#     x = random.uniform(0,50)
#     z = round(x,2)
#    punkty.append(z)
punkty= [ round(random.uniform(0,50), 2) for i in range(15)]
print(punkty)
print("Maksymalna ilość punktów: ", max(punkty))
print("Minimalna ilość punktów: ",min(punkty))
g = float(input("Podaj liczbę: "))
if g in punkty:
    print("Indeks nr: ", punkty.index(g))
else:
    print("Nie ma tych punktów na liście")
o = sum(punkty)
o / len(punkty)
print("Średnia punktów to: ", round((o),2))

list1=[]
list2=[]
for i in punkty:
    if i < g:
        list1.append(i)
else:
    list2.append(i)
print("Ile punktów jest powyżej średniej: ", len(list1))
print(list1)
list2 = [ i for i in punkty if > g ]
print("Ile punktów jest poniżej średniej: ", len(list2))
print(list2)

