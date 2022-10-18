# Napisz skrypt, który sprawdzi czy litera wprowadzona przez użytkownika jest duża czy mała.
x = input("wprowadz literę: ")
if len(x)>1 or len(x)==0:
    print("bład")
    exit()
if "a" <= x <= "z":
    print("mała litera")
elif "A" <= x <= "Z":
    print("duża litera")
else:
    print("nie jest literą")


