# Napisz funkcję potęga(), która podniesie wartości z pierwszej listy do potęg z drugiej listy. Sprawdź,
# czy listy są tej samej długości. Parametrami funkcji są dwie listy. Funkcja ma zwracać listę z wynikami.
def potega(a, b):
    c=[]
    if len(a) != len(b):
        return c
    for i in range(len(a)):
            c.append(a[i] ** b[i])
    return c
print(potega([2,3,4],[6,4,2]))
