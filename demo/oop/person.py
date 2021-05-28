class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __gt__(self, other):
        return self.age > other.age

    def __int__(self):
        return self.age

    @property
    def category(self):
        if self.age < 30:
            return "Young"
        elif self.age < 60:
            return "Middleage"
        else:
            return "Old"


p1 = Person("Bill", 40)
print(p1.category)
print(int(p1))
p2 = Person("Bill", 30)
print(str(p1))  # p1.__str__()
print(p1 == p2)  # p1.__eq__(p2)
print(p1 > p2)  # p1.__gt__(p2)

persons = [Person("A", 20), Person("C", 15), Person("B", 30)]

for p in sorted(persons):
    print(p)

for p in sorted(persons, key=lambda p: p.name):
    print(p)
