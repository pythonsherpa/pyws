class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"{self.name} says hello!")

person = Person("Jim", 22)
person.say_hello()

class Student(Person):
    def learn(self, language):
        print(f"{self.name} is learning {language}")

student = Student("Jim", 22)
student.learn("Java")


import datetime

class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = datetime.date.fromisoformat(birthdate)

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1
        return age

person = Person("Joris", "1985-12-04")
print(person.age())
