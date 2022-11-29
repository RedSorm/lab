#Grupa 2. Użytkownik podaje 5 liczb. Zapisz do listy tylko liczby z przedziału [-10, 10].
for i in range(5):
    x = input("Podaj liczby: ")
list=[]
if  x < -10:
    list.append(x)
elif x > 10:
    list.append(x)
print(list)