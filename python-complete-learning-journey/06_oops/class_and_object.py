"""Class and object basics"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name}, {self.age} years old."


# Practice (5):
# 1) Create a `Student` subclass with a `grade` attribute and a `status()` method.
# 2) Implement `__repr__` and `__eq__` for `Person`.
# 3) Add a classmethod `from_dict(cls, d)` to construct from a dict.
# 4) Add a property `is_adult` that returns True when age >= 18.
# 5) Serialize/deserialize a `Person` to/from JSON.
#
# Sample solutions (examples):
# Solution for 1 (Student subclass):
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
    def status(self):
        return f"{self.name}: grade {self.grade}"

# Solution for 4 (property):
@property
def is_adult(self):
    return self.age >= 18
Person.is_adult = is_adult

if __name__ == "__main__":
    p = Person('Alice', 30)
    s = Student('Bob', 16, 'B')
    print(p.greet())
    print(s.status(), 'adult=', s.is_adult)
