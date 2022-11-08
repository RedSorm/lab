#zad 6
x = 1
sum = 0
numOfStudents = int(input("Wprowadz liczbe studentow: "))
if numOfStudents <1:
    exit
    print("zła liczba studentów")
while True:
    if x>numOfStudents:
        break
    points = int(input(f"Wprowadz liczbe punktow studenta {x}: "))
    if points > 100 or points <0 :
        continue
    sum += points
    x+=1
median = sum/numOfStudents
print("Średnia punktów uczniów wynosi:", median)