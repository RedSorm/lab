#zad 5
x = 1
sum = 0
numOfStudents = int(input("Wprowadz liczbe studentow:"))
while x <= numOfStudents:
    points = int(input("Wprowadz liczbe punktow studenta"))
    sum += points
    x+=1
median = sum/numOfStudents
print("Średnia punktów uczniów wynosi:", median)