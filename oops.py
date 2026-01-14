#object oriented programming in python language
#class 
#object
#inheritence
#polymorphism
#abstraction
#encapsulation
# simple example using class , object and --init--() function

"""class person:
    def __init__(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place
    def details(self):
         return f"{self.name}({self.age})({self.place})"
p1 = person("pavan",20,"Duggirala")
print(p1.details())"""

#class creation object creation and class change and object change
"""class accounts:
    account1 = 121
    account2 = 122
    account3 = 123
accounts.account1 = 1
obj = accounts()
print(obj.account1)
print(obj.account2)
print(obj.account3)
obj = accounts()
print(obj.account1)
print(obj.account2)
print(obj.account3)"""

#using the init method and writing thr program
"""class Bankaccount:
    def __init__(self,accno,accname,ifsc,balance):
        self.accno=accno
        self.accname = accname
        self.ifsc = ifsc
        self.balance = balance
    def details(self):
        print(self.accno,self.accname,self.ifsc,self.balance)
object1 = Bankaccount(123,'pavan',12345,5000000)
object1.details()"""

# inheritance topic (EXAMPLE ENPLOYEES IN  A COMPANY FOR DIFFERENT ROLES)
"""class Employee():
    def __init__(self,emp_name,Id):
        self.emp_name=emp_name
        self.Id=Id
class Manager(Employee):
    def __init__(self,emp_name,Id,team_size):
        Employee.__init__(self,emp_name,Id)
        self.team_size=team_size
class Developer(Employee):
    def __init__(self,emp_name,Id,Programming_language):
        Employee.__init__(self,emp_name,Id)
        self.Programming_language=Programming_language
child1 = Manager("Pavan",122,5000)
child2 = Developer("Venkat",133,"HTML_CSS")

print(f"Manager:{child1.emp_name},Id:{child1.Id},team_size:{child1.team_size}")
print(f"Developer:{child2.emp_name},Id:{child2.Id},Programming_language:{child2.Programming_language}")
"""

#topic Iterator
#Return an iterator from a tuple, and print each value:
"""mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
      ( o r  ) 
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)
"""
#Strings are also iterable objects, containing a sequence of characters:

"""mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
       _( o r )
mystr = "banana"

for x in mystr:
  print(x)
"""

#Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):
"""class Mynumber:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
      x = self.a
      self.a +=1
      return x
myclass = Mynumber()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
"""

#StopIteration
"""class Mynumber():
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <=20:
            x = self.a
            self.a +=1
            return x
        else:
            raise StopIteration
myclass = Mynumber()
myiter = iter(myclass)
for x in myiter:
 print(x)
"""
##inheritance topic
"""class Faculty:
    def __init__(self, firstName, lastName, email, facultyId, address, mobileNumber, subjectsTeaching, salary, dateJoined):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.facultyId = facultyId
        self.address = address
        self.mobileNumber = mobileNumber
        self.subjectsTeaching = subjectsTeaching
        self.salary = salary
        self.dateJoined = dateJoined

    def getFullName(self):
        print(self.firstName + ' ' + self.lastName)

    def changeAddress(self, newAddress):
        self.address = newAddress
        print('Address changed successfully')

    def changeNumber(self, newNumber):
        self.mobileNumber = newNumber
        print('Mobile Number changed successfully')

    def getSalary(self):
        print('Your Salary is:', self.salary)"""

#accessing the same attributes or properties of the gives class to the same family subclass
"""class person():
    def __init__(self,surname,lastname,dob,gender,address,occupation,mobile):
      self.surname = surname
      self.lastnam = lastname
      self.dob = dob
      self.gender = gender
      self.address = address
      self.occupation = occupation
      self.mobile = mobile
    def get_full_name(self):
       print(self.surname+' '+self.lastnam)

    def change_address(self,new_address):
       self.address = new_address
       print("address changed successfully")

    def change_mobile(self,new_mobile):
       self.mobie = new_mobile
       print("mobile changed successfully")

    def change_gender(self,new_gender):
       self.gender = new_gender
       print("gender changed successfully")

class teenage(person):
   def __init__(self,surname,lastname,dob,gender,address,occupation,mobile,physically,girlfriend,boyfriend):
      self.physically = physically
      self.girlfriend = girlfriend
      self.boyfriend  = boyfriend
      person.__init__(self,surname,lastname,dob,gender,address,occupation,mobile)

      
class oldage(person):
   def __init__(self,surname,lastname,dob,gender,address,occupation,mobile,wife,husband):
      self.wife = wife
      self.husband = husband
      person.__init__(self,surname,lastname,dob,gender,address,occupation,mobile)

#creating the object and calling the function
teen1 = teenage(
    surname="Pavan",
    lastname="Krishna",
    dob="18-05-2005",
    gender="Male",
    address="Duggirala",
    occupation="Student",
    mobile="9876543210",
    physically="Fit",
    girlfriend="No",
    boyfriend="No"
)
#  Call methods to print output
teen1.change_address("Guntur")
teen1.change_mobile("9123456789")
teen1.change_gender("Male")
print(teen1.address)
print(teen1.mobile)
print(teen1.gender)"""


#printing the given array in the decreasing order of their frequency that means first find the frequency of the number and then decreasing order of that frequency
"""a = input("Enter the array elements: ")
b = a.split()
c = {}
for i in b:
    if i in c:
        c[i] += 1
    else:
        c[i] = 1
d = sorted(b, key=lambda x: (-c[x], b.index(x)))
d = [int(x) for x in d]  # Convert elements to integers
print(d)
"""

###printing the given array in the decreasing order of their frequency that means first find the frequency of the number and then decreasing order of that frequency
"""a = input("enter the numbers:")
b = a.split()
c = {}
for i in b:
    if i in c:
        c[i] += 1
    else:
        c[i] = 1
d = sorted(b, key=lambda x: (-c[x], b.index(x)))
d = [int(x) for x in d]
print(d)"""

##printhin true if the given number is amstrong or print false if it is not amstrong number
"""a = input("Enter the number:")
power = len(a)
b = list(a)
c = sum(int(i)**power for i in b)
if c == int(a):
    print("True")
else:
    print("False")"""

##Now writing the same code using the oops concepts in python
"""class ArmstrongNumber:
    def __init__(self, number):
        self.number = str(number)
        self.power = len(self.number)

    def is_armstrong(self):
        total = sum(int(digit) ** self.power for digit in self.number)
        return total == int(self.number)

# Example usage:
num = input("Enter a number: ")
armstrong = ArmstrongNumber(num)
print(armstrong.is_armstrong())"""

"""def checkArmstrong(mat, m, n):
    def is_armstrong(num):
        p = len(str(num))
        return sum(int(d) ** p for d in str(num)) == num

    result = []
    for row in mat:
        for num in row:
            if is_armstrong(num):
                result.append(num)
    return result

# Example
m = int(input("enter the m:"))
n = int(input("enter the n:"))
mat = []
for i in range(m):
    row = list(map(int, input(f"Enter the elements of row {i+1} (space-separated): ").split()))
    mat.append(row)

ans = checkArmstrong(mat, m, n)
if ans:
    print("Armstrong numbers:", ans)
else:
    print("No Armstrong numbers found")"""

## now finding the weather there is any armstrong number present in the given matrix without using the oops concept
"""a = int(input("Enter the number of rows:"))
b = int(input("Enter the number of coloumns:"))
mat = []  # Initialize mat as an empty list
for i in range(a):
    rows = list(map(int, input(f"Enter the elements of row {i+1} (space-separated): ").split()))
    mat.append(rows)
for row in mat:
    for i in row:
        power  = len(str(i))
        if sum(int(digit) ** power for digit in str(i)) == i:
            print("Armstrong number found:", i)
            break
    else:
        continue
    break
else:
    print("No Armstrong numbers found")"""

##sc
"""class TicketQueue:
    def __init__(self):
        self.queue = []
        self.customer_counter = 1

    def enqueue(self):
        self.queue.append(self.customer_counter)
        print(self.customer_counter)
        self.customer_counter += 1

    def dequeue(self):
        if self.queue:
            print(self.queue.pop(0))
        else:
            print("No customers in line")

    def display(self):
        print(" ".join(map(str, self.queue)))


if __name__ == "__main__":
    tq = TicketQueue()
    try:
        while True:
            action = int(input().strip())
            if action == 1:
                tq.enqueue()
            elif action == 2:
                tq.dequeue()
            elif action == 3:
                tq.display()
            else:
                print("Invalid option")
    except EOFError:
        pass
"""

##Encapsulation 
# In  this encapsulation there are 3 types of access specifiers they are 
# Public Access specifier
# Private access specifier 
# Proteced access specifier

## Now let us see the Public access specifier
"""class parent:
    publicData = 10
    def publicMethod(self):
        print(self.publicData)
class child(parent):
    def method(self):
        print(self.publicData)
obj1 = parent()
obj1.publicMethod()
print(obj1.publicData)
obj2 = child()
obj2.method()
print(obj2.publicData)"""


##modifying the class attributes
"""class students:
    def __init__(self,name,age,rollno):
        self.name = name
        self.age = age
        self.rollno = rollno
    count = 0
    def details(self):
        print(f"Name:{self.name}\nAge:{self.age}\nRollno:{self.rollno}")
        students.count += 1
        print(f"student count:{students.count}")

obj1 = students("pavan",20,1888)
obj1.details()"""

"""class Employee:
   def __init__(self, name="Bhavana", age=24):
      self.name = name
      self.age = age
   def displayEmployee(self):
      print ("Name : ", self.name, ", age: ", self.age)

print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__ )"""

## using the class method
#Mainly class method can be in 2 types they ar
#1. Using classmethod() Function
#2. Using @classmethod Decorator


## Encapsulation : combinig or grouping the related or set or things is known as Encapsulation
#in this encapsulation there are 3 types of access specifiers theya are
#1. Public access specifier
#2. private access specifier
#3. protected access specifier

# Public access specifier
"""class parent:
    public_data = 10
    def public_method(self):
        print(self.public_data)
class child(parent):
    def method(self):
        print(self.public_data)
obj1 = parent()
obj1.public_method()
print(obj1.public_data)
obj2 = child()
obj2.method()
print(obj2.public_data)"""

##Protected access specifier
# in this protected access specifier we can access the data in only in that class and in the sub class only.
# we need to use a singe underscore to make the data in protected access specifier
"""class parent:
    _protected_data = 20
    def _protected_method(self):
        print(self._protected_data)
class child(parent):
    def method(self):
        print(self._protected_data)
obj1 = parent()
obj1._protected_method()
obj2 = child()
obj2.method()
"""

## Private access specifier
# to use the private access specifier we need to use the double underscore in the class to make the data into private 
# in this private access specifier we can access the data in onl in that class only
"""class parent:
    __privatedata = 30
    def private_method(self):
        print(self.__privatedata)
class child(parent):
    def method(self):
        print(self._parent__privatedata)
obj1 = parent()
obj1.private_method()
obj2 = child()
obj2.method()"""

"""class A:
    __pavan = 10
    def privatemethod(self):
        print(self.__pavan)
class B(A):
    def method(self):
        print(self.__pavan)
obj1 = B()
obj1.method
print(obj1._A__pavan)"""

# Abstract Method 
#to use abstract method firstly we need to implemet the abstract "ABC" module in the abstract class then only we can use the abstract class
# and also if there are one or more than abstract methods in a class the that calss is called as abstract class
# if we need to create an object to the abstract class then firsty we need to inherit that calss in another calss then only we can able to create the abstract class
"""from abc import ABC,abstractmethod
import math
class polygon(ABC):
    @abstractmethod
    def sides(self):
        pass
    @abstractmethod
    def area (self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    def figure(self):
        return "It is a two dimensional figure"

class rectangle(polygon):
    def sides(self,length,breath):
        self.length = length
        self.breath = breath
    def area(self):
        return self.length*self.breath
    def perimeter(self):
        return 2*(self.length+self.breath)
    def extramethod(self):
        return "It has 4 sides!"
class triangle(polygon):
    def sides(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        s = (self.a+self.b+self.c)/2
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
    def perimeter(self):
        return self.a+self.b+self.c
    def extramethod(self):
        return "It has 3 sides!"
class square(polygon):
    def sides(self,a):
        self.a = a
    def area(self):
        return self.a*self.a
    def perimeter(self):
        return 4*self.a
    def extramethod(self):
        return"It has 4 sides!"
    
obj1 = rectangle()
obj1.sides(5,6)
obj2 = triangle()
obj2.sides(3,4,5)
obj3 = square()
obj3.sides(4)

for obj in (obj1,obj2,obj3):
    print (obj.area())
    print(obj.perimeter())
    print(obj.extramethod())
    print(obj.figure())
    """

## static variables vs instance variables 
#in classes there are three types of variables they are,
#1. Static vatiable
#2. Instance variable
#3. Local variable
## Local variable if a variable is defined inside of the method in a class then this variable is called as static variable
## Static variable (or) Class variable : If a variable is declared outside of the method in a class is known as static variable or clas variable
## if we need to access the static variable then we need to use "obj.staticvariablename" (or) "class name.static variable"
## if we need to update  the value in an instance variable then the syntax is "obj.instancevariablename = newvalue"
# local variable
"""class America:
    def __init__(self,Tesla,spacex):
        self.Tesla = Tesla
        self.spacex = spacex
obj = America("Elon Musk","Elon Musk")
print(obj.Tesla)        """

##static variable (or) class varaiable
"""class India:
    india = "Ratan Tata"
    Ratan_Tata1 = "Nano car"
    Ratan_Tata = "Business Tycoon"
    def details(India):
       pass
obj = India()
India.india = "Mukesh Ambani"
print(India.india)
print(obj.Ratan_Tata1)
print(obj.Ratan_Tata)
"""
#instance variable
"""class A:
    def __init__ (self,a,b):
        self.instancevariable1 = a
        self.instancevariable2 = b
obj = A(500,1000)
obj.instancevariable3 = 50
obj.instancevariable4 = 10
obj2 = A(100,200)
print(obj2.instancevariable1, "this is obj2")
print(obj.instancevariable2, "this is obj1")
"""

##instance method 
# The instance method is a function that belongs to a class and works with the object of that class .
# it always takes "self" as the first parameter,which represents the object calling it.
# Instance method = normal function inside the class
# it works with object data (self)
# Needs an object to call it
"""class car:
    def __init__(self, model, fuel, year):
        self.model = model
        self.fuel = fuel
        self.year = year

    def information(self):
     return f"Model:{self.model},Fuel:{self.fuel},Year:{self.year}"

# Instance method usage
obj = car("BMW", "PETROL", 2025)
print(obj.information()) 
"""

## class method
# A class method is a method that is bound to the class and not the instance of the class.
# It can access or modify class state that applies across all instances of the class.
# Class methods take 'cls' as the first parameter, which refers to the class itself.
# They are defined using the @classmethod decorator.
# Example:

"""class car:
    fuel = "petrol"
    model = 2025
    def __init__(self,carname,brand):
     self.carname = carname
     self.brand = brand
    @classmethod
    def change_details(cls,newname)
       change
"""

##Static method 
# A static method is a  method that does not belongs to the class or instance method.
## this static method is used for general tasks or general utility functions thta does not require any access to class or instance data.
## static method do not use any "self" or "cls" parameters
## agter creating a static class we need to use @staticmethod decorator to define a staic method.
"""class calculator:
    @staticmethod
    def add(a,b):
        return a+b
    @staticmethod
    def mul(a,b):
        return a*b
    @staticmethod
    def sub(a,b):
        return a-b
    @staticmethod
    def div(a,b):
        return a/b
print(calculator.add(1,2))
print(calculator.sub(1,2))
print(calculator.mul(1,2))
print(calculator.div(1,2))"""

##dunder methods
##dunder methods area lso called as magical methods or special methods
# we use these dunder methods to override the built in functions in python
# some of the dunder methods are
# __init__() : it is used to initialize the object
# __str__() : it is used to return a string representation of the object
# __add__() : it is used to override the + operator
# __len__() : it is used to override the len() function
# __del__() : it is used to delete the object
# __repr__() : it is used to return a string representation of the object for debugging
# __eq__() : it is used to override the == operator
# __lt__() : it is used to override the < operator
# __gt__() : it is used to override the > operator
# __le__() : it is used to override the <= operator
# __ge__() : it is used to override the >= operator
# __ne__() : it is used to override the != operator
# __call__() : it is used to make the object callable
# __getitem__() : it is used to access the elements of the object using the []
# __setitem__() : it is used to set the elements of the object using the []
# __delitem__() : it is used to delete the elements of the object using the
# __iter__() : it is used to make the object iterable
# __next__() : it is used to iterate the object
# __contains__() : it is used to override the in operator
# __hash__() : it is used to override the hash() function
# __bool__() : it is used to override the bool() function
# __format__() : it is used to override the format() function
# __copy__() : it is used to override the copy() function
# __deepcopy__() : it is used to override the deepcopy() function
# there are some of the dunder methods in python.
#__add__() method
"""class A:
    def __init__(self,a):
     self.a = a
    def __add__(self,b):
        return self.a +b.a
obj1 = A(10)
obj2 = A(20)
print(obj1+obj2)"""
#__mul__() method
"""class B:
    def __init__(self, a):
        self.a = a

    def __mul__(self, b):
        return self.a * b.a

obj1 = B(10)
obj2 = B(10)
print(obj1 * obj2)"""

#__isub__() method
"""class C:
    def __init__(self, a):
        self.a = a
    def __isub__(self, b):
        self.a = self.a - b.a
        return self
obj1 = C(20)
obj2 = C(10)
obj1 -= obj2
print(obj1.a)"""

#__*=__method
"""class D:
    def __init__(self,a):
        self.a = a
    def __imul__(self, b):
        self.a = self.a * b.a
        return self
obj1 = D(10)
obj2 = D(20)
obj1 *= obj2
print(obj1.a)"""

## module
## what is module?
# A module is a file containing Python code that defines functions, classes, and variables.
# use amodule
# we can use a module in two ways they are
# 1. import module
# 2. from module import function/class/variable
## creating a module
# to create a module we need to create a python file with .py extension and write the code in that file
## importing a module
# to import a module we need to use the import keyword followed by the module name
## biult in module
"""import platform
a = platform.system()
print(a)
b = platform.release()
print(b)
c = platform.version()
print(c)
d = platform.machine()
print(d)
e = platform.processor()
print(e)
f = platform.architecture()
print(f)"""


# USING THE dir() FUNCTION
# The dir() function is used to find out all the names in a module.
"""import platform
a = dir(platform)
print(a)"""


## date time module
# The datetime module supplies classes for manipulating dates and times.
# To use the datetime module, we need to import the datetime class from the datetime module.
"""import datetime
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.month)
print(x.strftime("%b"))
print(x.strftime("%B"))
print(x.strftime("%a"))
print(x.strftime("%A"))
"""

## python JSON
# JSON in python
# JSON stands for JavaScript Object Notation
# JSON is a syntax for storing and exchanging data
# JSON is text, written with JavaScript object notation
# JSON is a lightweight data interchange format
# JSON is language independent
# JSON is easy to read and write
import json
import math
#convert from json to python
"""x = '{"name":"pavan","age":20,"city":"duggirala"}'
y = json.loads(x)
print(y)"""

# converting from python to json
"""x = {
    "name":"pavan",
    "age":20,
    "city":"duggirala"

}
y = json.dumps(x)
print(y)"""

##Regular Expressions (or) Regex
# A regular expression is a special sequence of characters that helps you match or find other strings or sets of strings, using a specialized syntax held in a pattern.
# Regular expressions are used to check if a string contains the specified search pattern.
# we use "re" too import the regular expression (or) Refex
"""import re
x = "My name is pavan.I am 20 years old."
y = re.search("^My.*pavan$",x)
print(y)
z = re.findall("\d",x)
print(z)"""

# The sub() Function
# The sub() function replaces the matches with the text of your choice.
"""import re
x = "The rain in spain"
x = re.sub("\s","9",x)
print(x)"""
#You can control the number of replacements by specifying the count parameter:
"""import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)"""

# The split() function
#The split()function returns a list where the string has been split at each match.
"""import re
x = "The rain in spain"
x = re.split("\s",x)
print(x)"""

#and also we can specify the number of occurrences by specifying the "maxsplit" parameter.
"""import re
x = "The rai in spain"
x = re.split("\s",x,2)
print(x)"""

#Match object
# A match object is an object containing the information about the searc and the result.
# The match object has properties and methods used to retrieve information about the search, and the result.
# If there is no match, the value None will be returned, instead of the Match Object.
"""import re
x =  "The rain in spain"
x = re.search("ai",x)
print(x)"""
# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match
"""import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())"""

# Python PIP
# PIP is the package (or) module manager in the python packages or python modules
# to use the the pip first we need to install the pip in our python idle terminal (or) command prompt by using the below command
# python -m ensurepip
# after installing the pip we need to pgrade the pip by using the below command
# python -m pip install --upgrade pip
# after upgrading the PIP we can install any packaage (or) module by using the "pip install package(or) modukea name" command.
# To uninstall the package(or) module we need to use the command "pip uninstall package(or) module name"
# after installing the needed package or module in the python then we need to import that package or  module to access the functions and variables in that module (or) package.
# To list the installed packages ora modules in the python we shpuld use the command "pip list packages"
"""import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))"""

##Try-Except
#The try block lets you test a block of code for errors.
#The except block lets you handle the error.
#The finally block lets you execute code,regardless of the result of the try- and except blocks.
#The else block lets you execute code when there is no error.
"""try:
    print(x)
except:
    print("An exception occurred")

try:
    print("Hello")
except:
    print("something went wrong")
else:
    print("nothing went wrong")
finally:
    print("The try except is finished")
    # The finally block will always be executed, regardless of whether an exception occurred or not.
    print("The finally block is executed")
"""
## string formatting 
#string formatting is the process of inserting the valuess into the string
# There are three ways to format string in python
#1. using the % operator
#2. using the format() method
#3. using f-strings (formatted string literals)
# using the % operator
"""
name = "pavan"
class_name = "Btech"
age = 20
print("my name is %s.I am %d years old.I am studying %s"%(name,age,class_name))
"""

# using the format() method
"""
name = "pavan"
class_name = "Btech"
age = 20
print("my name is {}.I am {} years old.I am studying {}".format(name,age,class_name))
"""

# using f-strings
"""
name = "pavan"
class_name = "Btech"
age = 20
print(f"my name is {name}.I am {age} years old.I am studying {class_name}")"""

#Index Numbers
# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders.
"""
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))"""

#Named Indexes
#You can also use named indexes by entering a name inside the curly brackets {carname}, but then you must use names when you pass the parameter values txt.format(carname = "Ford"):
"""
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))"""

#Input Number
#The input from the user is treated as a string. Even if, in the example above, you can input a number, the Python interpreter will still treat it as a string.
#You can convert the input into a number with the float() function:
"""x = input("Enter a number:")

#find the square root of the number:
y = math.sqrt(float(x))

print(f"The square root of {x} is {y}")"""

#Validate Input
#The input provided by the user is always a string. If you want to accept a number, you should convert the string to a number.
#But what if the user writes text instead of a number? The conversion will fail, and the program will crash.
#To avoid this, use a try-except block to catch the error:
"""try:
    x = float(input("Enter a number:"))
    y = math.sqrt(x)
    print(f"The square root of {x} is {y}")
except ValueError:
    print("Invalid input. Please enter a numeric value.")  """

# virtual environment
# A virtual environment is a tool that helps to keep dependencies required by different projects in separate places, by creating virtual Python environments for them.
# It solves the "Project X depends on version 1.x but, Project Y needs 4.x" dilemma and keeps your global site-packages directory clean and manageable.
# To create a virtual environment we need to use the below command
# python -m venv myenv
# after creating the virtual environment we need to activate the virtual environment by using the below command
# for windows
# myenv\Scripts\activate
# for mac and linux
# source myenv/bin/activate
# after activating the virtual environment we can install the needed packages or modules in that virtual environment
# after installing the needed packages or modules in the virtual environment we can use those packages or modules
"""import cowsay
cowsay.cow("Hello, I'm a cow!")"""

## file handling methods
# File handling is an important part of any web application.
# Python has several functions for creating, reading, updating, and deleting files.
# To open a file in python we need to use the open() function
# The open() function takes two parameters; filename, and mode.
# There are four different methods (modes) for opening a file:
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)
# Example
""""with open("gpsk.txt","w") as f:
    f.write("hello pavan")
    f.write("\nhello sravan")
    f.write("\nhello bhanu")
with open("gpsk.txt","r") as f:
    print(f.read())
with open ("gpsk.txt","a") as f:
    f.write("\n good morning")  
with open("gpsk.txt","r") as f:
    print(f.read())
with open ("gpsk.txt","w") as f:
    f.write("gaddam")
    f.write("\n pavan")
    f.write("\n siva")
    f.write("\n krishna")
with open("gpsk.txt","r") as f:
    print(f.read())"""

#ATM machine dispenceary notes
2000, 500, 200, 100, 50, 20, 10, 5, 2, 1
a = 2000
b = 500
c = 200
d = 100
e = 50
f = 20
g = 10
h = 5
i = 2
j = 1
amount  = int (input('Enter the amoount:'))
