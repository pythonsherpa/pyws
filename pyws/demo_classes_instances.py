class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    def say_hi(self):
        return f"{self.name} says hi!"

    @classmethod
    def population_count(cls):
        return f"The total population is {cls.count}"



person = Person("Joris")
print(Person.count)
print(person.say_hi())
# print(Person.say_hi())
print(Person.population_count())
print(person.population_count())


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_string):
        year, month, day = date_string.strip().split("-")
        return cls(year, month, day)

d1 = Date(2026, 10, 1)
d2 = Date.from_string("2026-10-01")
print(d2.year)