# Napisz funkcję sum_of_values(), która policzy i zwróci sumę wartości (values) słownika:
# dict1 = {'data1':10, 'data2':-4, 'data3':2}
# Nie wolno korzystać z funkcji sum().


def sum_of_values(dict1):
    values = 0
    for i in dict1.values():
        values += i
    return values

dict1 = {'data1': 10.6, 'data2': -4, 'data3': 2}
print(sum_of_values(dict1))
