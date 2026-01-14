##class and object creation
"""class MohanBabuUniversity:
    def __init__(self, course, branch, Year, section, classroom):
        self.course = course
        self.branch = branch
        self.Year = Year
        self.section = section
        self.classroom = classroom

    def details(self):
        print(f"Course: {self.course}\nBranch: {self.branch}\nYear: {self.Year}\nSection: {self.section}\nClassroom: {self.classroom}")

course = input("Enter course: ")
branch = input("Enter branch: ")
Year = input("Enter year: ")
section = input("Enter section: ")
classroom = input("Enter classroom: ")

obj1 = MohanBabuUniversity(course, branch, Year, section, classroom)
obj1.details()"""

##inheritance 
#The inheritance is nothiing but to access the attributes and methoda from the already created class to newy created class is known as Inheritance
# The already created class is nothing but we call as Super class or parent class or Base class
#The newly created class we called it as  Derived claass or child class or sub class
#There are 5types or inheritances they are
#1.single inheritance
#2.multiple inheritance
#3.multilevel inheritance
#4.hierachial inheritance
#5.hybrid inheritance

##Single inheritance
"""class Father:
    def __init__(self,surname,bloodgroup):
        self.surname = surname
        self.bloodgroup = bloodgroup

class son(Father):
    def __init__(self,surname,bloodgroup,height):
        super().__init__(surname,bloodgroup)
        self.height = height
surname = input("entr the surname:")
bloodgroup = input("enter the bloodgroup:")
height = input("eneter the height in feet:")
obj1 = son(surname,bloodgroup,height)
print(f"SON details\nSurname:{obj1.surname}\nBloodgroup:{obj1.bloodgroup}\nHeight:{obj1.height}")
"""

#MULTIPLE inheritance
"""class Android:
    def __init__(self, Ram, Rom, Processor, Model, Cost, Battery, camera):
        self.ram = Ram
        self.rom = Rom
        self.processor = Processor
        self.model = Model
        self.cost = Cost
        self.battery = Battery
        self.camera = camera

    def android_features(self):
        print("Android Features:")
        print(f"RAM: {self.ram}, ROM: {self.rom}, Processor: {self.processor}, Model: {self.model}, Cost: {self.cost}, Battery: {self.battery}, Camera: {self.camera}")

class Iphone:
    def __init__(self, Ram, Rom, Processor, Model, Cost, Battery, camera):
        self.ram = Ram
        self.rom = Rom
        self.processor = Processor
        self.model = Model
        self.cost = Cost
        self.battery = Battery
        self.camera = camera

    def iphone_features(self):
        print("iPhone Features:")
        print(f"RAM: {self.ram}, ROM: {self.rom}, Processor: {self.processor}, Model: {self.model}, Cost: {self.cost}, Battery: {self.battery}, Camera: {self.camera}")

class Mobile(Android, Iphone):
    def __init__(self, Ram, Rom, Processor, Model, Cost, Battery, camera):
        Android.__init__(self, Ram, Rom, Processor, Model, Cost, Battery, camera)
        Iphone.__init__(self, Ram, Rom, Processor, Model, Cost, Battery, camera)

    def show_details(self):
        print("Mobile Details:")
        print(f"RAM: {self.ram}")
        print(f"ROM: {self.rom}")
        print(f"Processor: {self.processor}")
        print(f"Model: {self.model}")
        print(f"Cost: {self.cost}")
        print(f"Battery: {self.battery}")
        print(f"Camera: {self.camera}")

# Example usage
ram = input("Enter RAM: ")
rom = input("Enter ROM: ")
processor = input("Enter Processor: ")
model = input("Enter Model: ")
cost = input("Enter Cost: ")
battery = input("Enter Battery: ")
camera = input("Enter Camera: ")

mobile = Mobile(ram, rom, processor, model, cost, battery, camera)
mobile.show_details()
mobile.android_features()
mobile.iphone_features()
"""
##              (or)
"""class fly:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

class landing:
    def __init__(self, landing_speed):
        self.landing_speed = landing_speed

class emirates(fly, landing):
    def __init__(self, flying_speed, landing_speed):
        fly.__init__(self, flying_speed)
        landing.__init__(self, landing_speed)

    def details(self):
        print(f"flying speed: {self.flying_speed}\nlanding speed: {self.landing_speed}")

flying_speed = input("enter the flying speed: ")
landing_speed = input("enter the landing speed: ")
obj = emirates(flying_speed, landing_speed)
obj.details()"""

##method overriding
##in method overriding python does not support the method overriding because python is dynamically types language soo to ake the method overloading supportedin pythn we use multiple dispatch method
"""from multipledispatch import dispatch       
class A:
    @dispatch(int, int)
    def add(self, a, b):
        return a + b

    @dispatch(int, int, int)
    def add(self, a, b, c):
        return a + b + c

obj = A()
print(obj.add(1, 2))
print(obj.add(1, 2, 3))"""
