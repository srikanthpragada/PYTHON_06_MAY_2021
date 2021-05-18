def display(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


def show(*args, **kwargs):
    pass


display(a=10, b=20, name='Point')
display(r=10, x=10, y=20)
show(10, 20, name='Point')
