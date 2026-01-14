"""Inheritance examples"""

class Animal:
    def speak(self):
        return '...'

class Dog(Animal):
    def speak(self):
        return 'woof'


# Practice (5):
# 1) Implement a multiple inheritance example (mixins + base class).
# 2) Explore and print the method resolution order (MRO) for a class.
# 3) Override __init__ in subclass and call super().__init__ correctly.
# 4) Demonstrate polymorphic behavior through a collection of Animals.
# 5) Use composition instead of inheritance for a similar behavior and compare.
#
# Sample solutions (examples):
class Flyer:
    def fly(self):
        return 'flying'

class Bird(Animal, Flyer):
    def speak(self):
        return 'tweet'

# show MRO
def show_mro(cls):
    return [c.__name__ for c in cls.__mro__]

if __name__ == "__main__":
    d = Dog()
    b = Bird()
    print(d.speak(), b.speak(), b.fly())
    print('Bird MRO:', show_mro(Bird))
