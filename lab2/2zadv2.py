# Napisz skrypt, który sprawdzi czy litera wprowadzona przez użytkownika jest duża czy mała.
x = input("wprowadz literę: ")
if len(x)>1 or len(x)==0:
    print("bład")
    exit()
n=ord("a")-ord("A")
if "a" <= x <= "z":
    print(chr(ord(x)-n))
elif "A" <= x <= "Z":
    print(chr(ord(x)+n))
else:
    print("nie jest literą")
