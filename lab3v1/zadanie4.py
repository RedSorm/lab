#Zmodyfikuj program z zad. 1 tak, aby przechodząc po kolejnych liczbach przedziału, wypisywać
#tylko liczby parzyste, a nieparzyste – pomijać. Użyj instrukcji continue
a = int(input("Wprowadz pierwszą liczbę: "))
b = int(input("Wprowadź drugą liczbę: "))
if(a>b):
    c=b
    d=a
else:
    c=a
    d=b
while(c<=d):
    if c%2:
        c+=1
        continue
    print(c, end="," )
    c+=1