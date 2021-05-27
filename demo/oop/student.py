class Student:
    # Static attribute or class attribute
    courses = {'python': 5000, 'ds': 10000, 'django': 3000}
    taxrate = 10

    @staticmethod
    def getfee(course):
        fee = Student.courses[course]
        return fee + fee * Student.taxrate / 100

    def __init__(self, name, course='python', feepaid=0):
        # object attributes
        self.name = name
        self.course = course
        self.feepaid = feepaid

    def payment(self, amount):
        self.feepaid += amount

    def getdue(self):
        return Student.getfee(self.course) - self.feepaid


print(Student.getfee('ds'))  # Call static method
s1 = Student("Jack")
s2 = Student("Mike", 'ds', 5000)
s1.payment(3000)
print(s1.getdue())
print(s2.getdue())
