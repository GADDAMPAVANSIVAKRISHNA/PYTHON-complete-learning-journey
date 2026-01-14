#name = "John"
#print("Hello",name,sep=",",end="!" )

#number = input("Enter the number: ")
#print("You entered:",number)

#num = float(input("enter your num: "))
#print("Value of Pi:",num)


"""numbers = input("enter the numbers:")
x,y,z = numbers.split(" ")
sum = int(x)+int(y)+int(z)
print("sum of input:",sum)"""

#a=input()
#x,y,z=a.split(" ")
#sum = int(x)+int(y)+int(z)
#print("sum of input:",sum)

'''name = input("enter your name: ")
age = input("enter your age: ")
print("Name:"+name,"age:"+age, sep=",")

a = input("enter the number:")
print("Countdown:"+a,"Blast Off",end="!")
a,b = input("enter the number:").split(" ")
print("addition:"+str(int(a)+int(b)),"multiplication:"+str(int(a)*int(b)),"subtraction:"+str(int(a)-int(b)),"division:"+str(int(a)/int(b)))

a,b = input("enter the number:").split(" ")
print("10>5:"+str(int(a)>int(b)),"10<5:"+str(int(a)<int(b)),"10==5:"+str(int(a)==int(b)),"10!=5:"+str(int(a)!=int(b)),sep=",")
'''
"""a, b = input("enter the values:").split(",")
print("True and False:"+ str(bool(a) and bool(b)),"True or False:"+str(bool(a) or bool(b)),"not true:"+str(not bool(a)))"""

"""a, b = input("Enter the values separated by comma: ").split(",")
print("True and False: " + str(bool(a) and bool(b)))
print("True or False: " + str(bool(a) or bool(b)))
print("not True: " + str(not bool(a)))"""

"""inp = input("Enter the string: ")
print("You entered:"+inp)"""

"""num1 = input("num1:")
num2 = input("num2:")
sum = int(num1) + int(num2)
print(f"Sum:{sum}")"""

"""a = input("radius:")
pi = 3.14
area = pi*float(a)**2
print(f"Area of circle:{area}")"""


"""a = int(input("enter the value:"))
b = int(input("enter the value:"))
c = int(input("enter the value:"))
d = b**2-4*a*c
print(f"Roots:{(-b+d**0.5)/2*a,(-b-d**0.5)/2*a}")"""

"""a = input("enter the value of a:")
b = input("enter the value of b:")
temp = a
a = b
b = temp
print(f"After swapping: a={a}, b={b}")"""

"""a = input("Enter the value of temperature in celcius: ")
Farhenheat =(float(a) *9/5)+32
kelvin = float(a)+273.5

print(f"Temperature in Farhenheat: {Farhenheat}, Temperature in Kelvin: {kelvin}")"""


"""a = input("Enter the amount in usd:")
b = input("Enter the exchange rate usd to eur:")
amount = float(a)*float(b)
print(f"Equivalent amount in EUR: {amount}")"""

"""a = input("enter the 1st digit:")
b = input("enter the 2nd digit:")
operation = input("enter the operation:")
if operation == "+":
    print(f"sum:{int(a)+int(b)}")
elif operation == "-":
    print(f"subtraction:{int(a)-int(b)}")
elif operation == "*":
    print(f"multiplication:{int(a)*int(b)}")
elif operation == "/":
    print(f"division:{int(a)/int(b)}")
else:
    print("Invalid operation. Please enter +, -, *, or /.")
print("Thank you for using the calculator!")
"""

"""s = input("Enter a string:")
print(s[1])
print(s[-1])
print(s[1:-1])
print(s[:3])
print(s[2:])
print(s[:-1])
print(s[::2])
print(s[1::2])
print(s[::-1])
print("end of code")
"""
#string concatenationexample
"""first_name = "pavan"
second_name = "kumar"
full_name = first_name+" "+second_name
print(full_name)"""

"""myspace = "Hello World is Myne"
print(str.lstrip(myspace))
print(str.rstrip(myspace))"""

#string formatting methodsname = input("enter the name:")
"""age  = input("enter the age:")
clas = input("enter the class:")
print("My name is %s and My age is %d and I am studying in %s class."%(name,int(age),clas))
print("My name is {} and My age is {} and I am studying in the {} class.".format(name,age,clas))
print(f"my name is {name} and my age is {age} and I am studying in {clas} class.")"""

# escape sequences
#print('indie\'s westie\'s \v american\'s')


#example problems on strings+numbers+decision making
"""s =input("enter the string:")
s2 =s.lower()
a=s2.count("a")
e=s2.count("e")
i=s2.count("i")
o=s2.count("o")  
u=s2.count("u")
print(f"Number of vowels :{a+e+i+o+u}")"""

#GRADE CALCULATOR
"""s1 = input("enter the marks in maths:")
s2 = input("enter the marks in science:")
s3 = input("enter the marks in english:")
s4 = int(s1)+int(s2)+int(s3)
s5 = s4/3
print(f"Total marks: {s4}")
print(f"Average marks: {s5}")
if s5 >= 90:
    print("Grade: A")
elif s5 >= 80:
    print("Grade: B")
print("code ended here")
"""

# finding the given string is apalindrome or not
"""s = input("enter the string:")
s2 = s[::-1]
print(f"Reversed string: {s2}")
if s == s2:
    print("The given string is a palindrome")
else:
    print("The given string is not a palindrome")
print("code ended here")"""

#finding the largest number in the given three numbers
"""a = int(input("enter the number 1:"))
b = int(input("enter the number 2:"))
c = int(input("enter the number 3:"))
if a>b and a>c:
    print(f"{a} is the largest number")
elif b>a and b>c:
    print(f"{b} is the largest number")
elif c>a and c>b:
    print(f"{c} is the largest number")
else:
    print("All numbers are equal")"""


#checking the given number is a leap year or not
"""a = int(input("enter the year:"))
if(a%4==0 and a%100!=0) or (a%400==0):
    print("the given number is a leap yeat")
else:
    print("the given number is not a leap year")"""

#temperature calculater

"""a = int(input("enter the temperature:"))
b = input("enter the units:")
if b=="c" or b=="C":
    f =(a*9/5)+32
    k = a + 273.15
    print(f"temperature in farenheit:{f}, temperature in kelvin: {k}")
elif b=="f" or b=="F":
    c = (a-32)*5/9
    k = c + 273.15
    print(f"temperature in celcius:{c}, temperature in kelvin: {k}")
elif b=="k" or b=="k":
    c = a - 273.15
    f = (c * 9/5) + 32
    print(f"temperature in celcius:{c}, temperature in farenheit: {f}")
else:
    print("Invalid unit. Please enter C, F, or K.")"""


    # using while loop and for loop and also using break statement 

"""Tokens = 15
while Tokens < 5:
    print("you got the token")
    Tokens-= 1"""

# for loop
"""Tokens = 15
for i in range(0, Tokens >= 5):
    print("you got the token")
print ("code ended here")"""

# print numbers for 1 to n

"""a = int (input("enter the number:"))
for i in range (1, a+16):
 print(i)"""

# calculatinfg the sum of natural nubers

"""a = int (input("enter the number:"))
i = 1
sum = 0
while i<=a:
    sum += i
    i += 1
print(sum)"""

# printing the even numbers from n  natural numbers
"""a = int(input("enter the number:"))
print(f"even numbers form 1 to {a} are:")
for i in range(1, a+1):
    if i%2 == 0:
        print(i)"""

# print odd numbers from the 1 to n natural numbers
"""a = int(input("enter the number:"))
print(f"odd numbers form 1 to {a} are:")
for i in range(1,a+1):
    if i % 2 != 0:
      print(i)"""

#printing the multiplication of the f=given n number
"""n = int(input("enter the value"))
i = 1
for i in range(1, i+10):
 print(f"{n}x{i}={n*i}")"""

#printing the factorial of the number
"""n = int(input("enter the number:"))
fact = 1
for i in range(1, n+1):
    fact *= i
    print(f"{fact}")"""

# solving the problems using the functions
"""def add(a,b):
    print(a+b)
add(5,10)
    #(or)
a = input("enter the first number:")
b = input("enter the second number:")
def add(a,b):
    sum = int(a)+int(b)
    return sum
print(add(a,b))"""
 # area of the circle
"""a = float(input("enter the pi value:"))
b = int(input("enter the radius:"))
def area_of_circle(a,b):
    area = a*(b**2)
    return area
print(f"area of the circle is:{area_of_circle(a,b)}")"""

"""def twoSum(nums, target):
    num_map = {}  

    for index, num in enumerate(nums):
        complement = target - num  

        if complement in num_map:
            return [num_map[complement], index]  
        num_map[num] = index
"""

# find the rots of the quadratic eqation ax^2 + bx + c = 0
"""a = int(input("enteer the value of a:"))
b = int(input("enter the value of b:"))
c = int(input("enter the value of c:"))
def roots_of_quadratic(a, b, c):
    d = b**2 - 4*a*c
    e = d**0.5
    root1 = (-b + e) / (2 * a)
    root2 = (-b - e) / (2 * a)
    return root1, root2
print(f"The roots of the quadratic equation are: {roots_of_quadratic(a, b, c)}")
    """
#swapping of two numbers using functions
"""def swap_numbers(a, b):
    temp = a
    a = b
    b = temp
    return a, b
a = input("Enter the value of a: ")
b = input("Enter the value of b: ")
a, b = swap_numbers(a, b)
print(f"After swapping: a={a}, b={b}")"""

# temperature conversion using functions
"""c = int(input("enter the temperatre in celcius:"))
def temperature_conversion(c):
    f = (c * 9/5) + 32
    k = c + 273.15
    return f, k
f, k = temperature_conversion(c)
print(f"Temperature in Fahrenheit: {f}, Temperature in Kelvin: {k}")"""

# list concatenation
"""input_values = input("Enter the values separated by commas: ")
l = (int(value)for value in input_values.split(","))
print(l):"""

#creating a set 
"""empty_set = set()
a = [1,2,3,4,5]
print()"""

# creating a dictionary
"""my_dict = {'name': 'pavan', 'age': '20', 'place':'Duggirala'}
print(my_dict)
"""
#accessing the values
"""d = {'name': 'pavan', 'age': '20', 'place':'Duggirala'}
name_value = d['name']
age_value = d['age']
print(name_value,age_value)"""

#adding and modigind the value in the dictionary
"""d = {'name': 'pavan', 'age': '20', 'place':'Duggirala'}
d['goal'] = 'software_engineer'
d['age'] = 18
print(d)"""

# practicing methods of the dictionary
"""d = {'name':'pavan', 'age':'20', 'place':'duggirala', 'goal':'software engineer'}
print(d.keys())

d = {'name':'pavan', 'age':'20', 'place':'duggirala', 'goal':'software engineer'}
print(d.values())

d = {'name':'pavan', 'age':'20', 'place':'duggirala', 'goal':'software engineer'}
print(d.items())

d = {'name':'pavan', 'age':'20', 'place':'duggirala', 'goal':'software engineer'}
print(d.get('name'))

d = {'name':'pavan', 'age':'20', 'place':'duggirala', 'goal':'software engineer'}
print(d.pop('goal'))
print(d)

d = {'name':'pavan', 'age':'20', 'place':'duggirala', 'goal':'software engineer'}
print(d.update({'place':'hyderabad'}))
print(d)
"""
#dictionary comprehension
"""square_roots = {x:x**2 for x in range (1,6)}
print(square_roots)"""

#dictionaries using looping statements
"""d = {'name':'pavan', 'age':'20', 'place':'duggirala', 'goal':'software engineer'}
for key in d(key):
    print(key)
for values in d(values):
    print(values)
for items in d(items):
    print(items)"""

#problems on sum of elements in the list
"""a = input("enter the numbers:")
b = [int(x) for x in a.split()]
print(b)
print(sum(b))"""

#print he max and min values in the list
"""a = input("enter the values:")
b = [int(x) for x in a.split()]
print(f"maximum:{max(b)}, minimum:{min(b)}")
"""
"""a = input("enter the values:")
l = [int(x) for x in a.split()]
l.sort()
print(l)
print(f"maximum:{l[-1]}, minumum:{l[0]}")"""

# removing the duplicate numbers from the list and printhing the list
"""a = input("enter the values:")
b = [int(x) for x in a .split()]
duplicate_numbers = list(set(b))
duplicate_numbers.sort()
print(duplicate_numbers)"""

# to delete the duplicate numbers in the list
"""a = input("enter the numbers:")
b = [int(x) for x in a.split()]
newl = []
for i in b:
    if i in newl:
        continue
    else:
        newl.append(i)
print(newl)
"""

#checking the number of occurrence of the number in the list
"""a = input("enter the numbers:")
b = [int(x) for x in a.split()]
num = int(input("Enter the number to count: "))
print(f"{num} occurs {b.count(num)} times in the list.")
print(b)
"""

"""seta = set(map(int, input("enter the values for set A (space separated): ").split()))
setb = set(map(int, input("enter the values for set B (space separated): ").split()))
c = seta.union(setb)
d = seta.intersection(setb)
print("Union:", c)
print("Intersection:", d)"""

# set
"""a = {1,2,3,4,5}
b = {6,7,8,9,10}
c = a.union(b)
d = a.intersection(b)
print("Union:", c)
print("Intersection:", d)"""

#dictionary in python using access the values, update the values and iterate the key values in the dictionary set
"""a = {'name':'John','age': '30','place': 'New York'}
print (f"Name : {a['name']}")
a['place'] = 'Sanfrancisco'
print(f"city:{a['place']}")
a['age'] = 31
print(f"age:{a['age']}")"""

"""
n = int(input("Enter the number"))
factorial = 1
while n>0:
    factorial = factorial*n
    n -= 1
print("Factorial of the number:", factorial)
"""

# prinnting the resume format they should select the format
"""print("Welcome to the Resume Builder")
print("Please select the Format of Your Resume")
print("1. PDF Format")
print("2. Word Format")
print("3. Just Text Format")
choice = input("enter your choice(1 or 2 or 3):")
while choice == '1' or choice == '2' or choice == '3':
    if choice == '1':
        print("You have been selected the PDF")
    elif choice == '2':
        print("You have been selected the Word")
    elif choice == '3':
        print("You have been selected the Plain Text")
else:
    print("Invalid choice. Please select a valid format.")
    """

##printing the  division of 2 numbers in case of the result is infinity then useing exception handling 
## Mainly exception handling is based on 4 Words they are,
# 1.try
# 2.except
# 3.else
# 4.finally

"""a = float(input("Enter the divisor number:"))
b = float(input("Enter the dividend number:"))
try:
    division = a / b
    print(division)
except :
    print("Cannot divide by Zero!")
else:
    print("Division Successfull !")
finally:
    print("This will always run!")
"""

#printing the stars with 6rows and 6 coloums
"""rows = 15
for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()"""

##again doing tthe same progra,
"""rows = int(input("Enter the number of rows:"))
for i in range (rows):
    for j in range(rows-i-1):
        print(" ", end="")
    for j in range(2*i+1):
        print("*",end="")
    print()"""


