class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"


p1 = Person("Bill", 30)
p2 = Person("Bill", 30)
print(str(p1))  # p1.__str__()
print(p1 == p2)
