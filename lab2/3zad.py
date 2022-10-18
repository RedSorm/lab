print('''Jaką operację chcesz wykonać?
1) dodawanie
2) odejmowanie
3) mnożenie
4) dzielenie
5) potęgowanie''')
C=int(input("Podaj numer operacji: "))
try:
    a=float(input("Podaj a: "))
except:
    print("została podana niepoprawna wartość")
    exit()
try:
    b=float(input("Podaj b: "))
except:
    print("została podana niepoprawna wartość")
    exit()
if C==1:
    print("Wynik wynosi: ", a + b)
elif C==2:
    print("Wynik wynosi ", a - b)
elif C==3:
    print("Wynik wynosi ", a * b)
elif C==4:
    if b==0:
        print("nie można dzielić przez 0")
        exit()
    print("Wynik wynosi ", a / b)
elif C==5:
    print("Wynik wynosi ", a ** b)
else:
    print("Brak operacji z podanym numerem")
