class StackFullError(Exception):
    def __str__(self):
        return "Stack is full!"


class StackEmptyError(Exception):
    def __str__(self):
        return "Stack is empty!"


# Iterator
class Stack_Iterator:
    def __init__(self, data):
        self.data = data
        self.pos = len(data) - 1

    def __next__(self):
        if self.pos < 0:
            raise StopIteration

        self.pos -= 1
        return self.data[self.pos + 1]

# Iterable
class Stack:
    def __init__(self, max_length=None):
        self.data = []
        self.max_length = max_length

    @property
    def length(self):
        return len(self.data)

    def push(self, value):
        if self.max_length is not None:
            if self.length == self.max_length:
                raise StackFullError()

        self.data.append(value)

    def pop(self):
        if self.length == 0:
            raise StackEmptyError()

        return self.data.pop()

    def peek(self):
        if self.length == 0:
            raise StackEmptyError()

        return self.data[-1]

    def __iter__(self):
        return Stack_Iterator(self.data)

# Testing
s = Stack()
s.push(10)
s.push(20)
s.push(30)

for n in s:
    print(n)

# stack empty error
print(s.pop())
print(s.pop())
# s.pop()
