# Napisz program działający jak prosty kalkulator. W tym celu utwórz funkcje dodawanie(),
# odejmowanie(), mnożenie() oraz dzielenie(). Następnie utwórz słownik, którego kluczem jest działanie, a
# wartością – nazwa odpowiedniej funkcji.
# Uwaga: funkcja jest obiektem, a nazwa funkcji – nazwą (referencją) tego obiektu
def dodawanie(a,b):
    return a + b
def odejmowanie(a,b):
    return a - b
def mnożenie(a,b):
    return a * b
def dzielenie(a,b):
    if b == 0:
        return
    else:
        return a / b
kalkulator = {"+":dodawanie,"-":odejmowanie,"*":mnożenie,"/":dzielenie}
u1 = float(input("Wprowadź piewszą liczbę: "))
u2 = float(input("Wprowadź drugą liczbę:  "))
działania= input("Podaj działanie: ")

print(kalkulator[działania](u1,u2))