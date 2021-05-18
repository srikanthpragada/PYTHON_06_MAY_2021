def wish(*names, message="Hi"):
    for n in names:
        print(message, n)


def f1(p1, *values, p2):
    pass


f1(10, 10, 20, p2=1)

wish("Scott", "Mark", "Larry", message="Hello")
wish("Harry", "Mike", 10)
