class Person:
    def __init__(self, name):
        self.name = name

person = Person("Erwin")
print(person.name)

# class Person:
#     def __init__(self, name):
#         self.set_name(name)
#
#     def get_name(self):
#         return self._name
#
#     def set_name(self, value):
#         if len(value) <= 1:
#             raise ValueError("The name is too short")
#         self._name = value
#
# person = Person("Erwin")
# print(person.get_name())

class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self._name

    def set_name(self, value):
        if len(value) <= 1:
            raise ValueError("The name is too short")
        self._name = value

    name = property(get_name, set_name)

person = Person("Jim")
print(person.name)
# person.name = "J"


class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) <= 1:
            raise ValueError("The name is too short")
        self._name = value

person = Person("Luuk")
print(person.name)