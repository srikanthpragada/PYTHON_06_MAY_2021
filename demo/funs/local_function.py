g = 100  # Global variable


def f1():
    global g
    a = 5  # Enclosing
    g = 200

    # Local function
    def f2():
        nonlocal a
        a = 1
        b = 10  # Local variable
        print(g, a, b)

    print(a)
    f2()
    print(a)


f1()
