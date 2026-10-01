from functools import total_ordering


@total_ordering
class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __eq__(self, other):
        return self.height == other.height

    def __lt__(self, other):
        return self.height <= other.height

p1 = Person("Bob", 180)
p2 = Person("Alice", 175)

print(p1 <= p2)
