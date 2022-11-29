def zad3(*args):
    print(args)
    for i in args:
        print(i)
    print()


def max(*args):
    m = args[0]
    for i in args:
        if m < i:
            m = i
    return m
print(max())


