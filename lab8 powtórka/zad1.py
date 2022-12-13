#. Napisz funkcję find(), która w liście sprawdza czy występuje podana wartość. Lista i wartość są
#parametrami funkcji. Funkcja ma zwracać listę indeksów, pod którymi wystąpiła wartość. Nie wolno korzystać z
#operatora in w celu sprawdzenia czy wartość występuje w liście


# def find(list1,int1):
#     list2=[]
#     for i in range(len(list1, int1)):
#             if list1[i] == int1:
#                 list2.append(i)
#     return(list2)
#
# print(find([1,4,6,7,8,9],8))
# print(find("samochód", "a"))
def find(list8_1, int8_1):
    list8_1_i = []
    for i in range(len(list8_1)):
        if list8_1[i] == int8_1:
            list8_1_i.append(i)
    return(list8_1_i)
print(find([1, 8, 5, 8, 42], 7))
print(find("samochód", "a"))