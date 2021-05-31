from abc import ABC, abstractmethod


# Abstract class
class Person(ABC):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def show(self):
        print(self.name)
        print(self.email)

    @abstractmethod
    def getoccupation(self):
        pass


class Student(Person):
    def __init__(self, name, email, course, college):
        super().__init__(name, email)  # Superclass init
        self.course = course
        self.college = college

    # Overriding
    def show(self):
        super().show()
        print(self.course)
        print(self.college)

    def change(self, course=None, college=None):
        if course is not None:
            self.course = course
        if college is not None:
            self.college = college

    def getoccupation(self):
        return f"Studying {self.course} at {self.college}"


class Employee(Person):
    def __init__(self, name, email, job, company):
        super().__init__(name, email)  # Superclass init
        self.job = job
        self.company = company

    def show(self):
        super().show()
        print(self.job)
        print(self.company)

    def change(self, job=None, company=None):
        if job is not None:
            self.job = job
        if company is not None:
            self.company = company

    def getoccupation(self):
        return f"Working as {self.job} in {self.company}"


class OnsiteEmployee(Employee):
    def __init__(self, name, email, job, company, client):
        super().__init__(name, email, job, company)  # Superclass init
        self.client = client

    def show(self):
        super().show()
        print(self.client)

    def change(self, job=None, company=None, client=None):
        super().change(job, company)
        if client is not None:
            self.client = client


s = Student("Bob", "bob@gmail.com", "MS CS", "Stanford")
s.change(course="MS IS")
s.show()
print(s.getoccupation())

e = OnsiteEmployee("Jack", "jack@yahoo.com", "Prog", "TCS", "Google")
e.change(client="Twitter")
e.show()

print(isinstance(s, Student), isinstance(s, Person))
print(issubclass(Student, Person), issubclass(Employee, Student))
