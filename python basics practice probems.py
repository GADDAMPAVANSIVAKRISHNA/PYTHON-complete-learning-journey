# sum of the digits
"""a = input("enter the number:")
sum = 0
for i in a:
    sum += int(i)
print("Sum of digits:", sum)"""

#reverse of a number
"""a = input("Enter the number: ")
reverse = a[::-1]
print("Reverse of the number:", reverse)
"""

#factorial of a number
"""n = int(input("enter the value"))
factorial = 1
while n > 0:
    factorial = factorial * n
    n = n - 1
print(factorial)"""

#printing the middle characters of the given string or a number
"""a = input("enter the string or number")
length = len(a)
if length % 2 == 0:
    # For even length, get the two middle characters
    middle_chars = a[length // 2 - 1 : length // 2 + 1]
else:
    # For odd length, get the single middle character
    middle_chars = a[length // 2]
print(middle_chars)"""

#printhing equal if ist digit + last digit == sum or middle digits equal or not 
"""a = input("enter the digits")
fd_ld = int(a[0]) + int(a[-1])
sum_middle = 0
for digit in a[1:-1]:
    sum_middle += int(digit)
if fd_ld == sum_middle:
    print("equal")
else:
    print("not_equal")"""

# check whether the digits in-between the first and last
#digit are less than first and last digit, if yes then print true, otherwise print
#false. 
"""a  = input('enter the number:')
b = a[0]
c = a[-1]
for digit in a[1:-2]:
    if digit<b:
        if digit<c:
            print(True)
    else:
        print(False)"""

# printing all the vowels in the string
"""s = input("enter the string: ")
vowels = [ch for ch in s if ch.lower() in "aeiou"]
if vowels:
    print("Vowels in reverse order:", ''.join(vowels[::-1]))
else:
    print("No vowels found.")"""

"""s = input("enter the string:")
s2 = s.lower()
vowels = [ch for ch in s2 if ch in "aeiou"]
print("vowels are:", ','.join(vowels))"""

#printing the vowels inthe string by avoiding the repeated vowel inthe string
"""a = input("enter the string:")
a2 = a.lower()
vowels = []
for ch in a2:
    if ch in "aeiou" and ch not in vowels:
        vowels.append(ch)
print(f"vowels in the string:", ','.join(vowels))"""

#remove the suplicate values in the string and print the unique value only
"""a = input("enter the string:")
a2 = a.lower()
b = []
for ch in a2:
    if a2.count(ch) == 1:
        b.append(ch)
print(f"words are: {','.join(b)}")"""

#upper case letters to lower case and lower case letters to the upper case letters
"""a = input("enter the string:")
result = ""
for ch in a:
    if ch.islower():
        result += ch.upper()
    elif ch.isupper():
        result += ch.lower()
    else:
        result += ch
    
print("Converted string:", result)"""

#printing the reverse order ofthe upper case letters first and then lower case in order
"""a = input("enter the string:")
upper_chars = [ch for ch in a if ch.isupper()]
lower_chars = [ch for ch in a if ch.islower()]
result = ''.join(upper_chars[::-1]) + ''.join(lower_chars)
print(result)
"""

#printing the highest value in the list
"""a = input("enter the numbers:").split(",")
numbers = [int(i) for i in a]
highest = max(numbers)
print("Highest value is:", highest)"""

#printing the seconnd highest number
"""a = input("enter the number:").split(",")
numbers = [int(i) for i in a]
unique_numbers = list(set(numbers))
if len(unique_numbers)<2:
    print("no second highest nuber")
else:
    unique_numbers.sort(reverse=True)
    print(unique_numbers[1])"""

#print the sum of all the numbers in the array
"""a = input("enter the numbers:").split(",")
numbers = [int(i) for i in a]
sum = 0
for i in numbers:
    sum+=i
print(sum)"""

# removing the duplicate numbers and printing the numbers
"""def remove_duplicates_from_input():
    a = input("enter the numbers:").split(",")
    b = [int(i) for i in a]
    unique_numbers = list(set(b))
    print(unique_numbers)"""

#checking the given list of elements are in the ascending order or not
"""def is_sorted_ascending(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

a = input("enter the numbers:").split(",")
numbers = [int(i) for i in a]
if is_sorted_ascending(numbers):
    print(True)
else:
    print(False)"""

#or 
"""def is_sorted_ascending(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr) - 1))
a = input("enter the array of elements:").split(",")
numbers = [int(i) for i in a]
if is_sorted_ascending(numbers):
    print(True)
else:
    print(False)"""
# Write a function to reverse the elements in an array. 
"""def reverse_array(arr):
    return arr[::-1]

# Example usage:
a = input("Enter the array elements separated by commas: ").split(",")
numbers = [int(i) for i in a]
reversed_numbers = reverse_array(numbers)
print("Reversed array:", reversed_numbers)"""

# removing the falsy values in the array
"""def remove_falsy_values():
    a = input("enter the values:")
    falsy_values = {"false", "0", "", "null", "undefined", "NaN"}
    filtered = [i for i in a if i.strip().lower() not in falsy_values]
    print(filtered)"""

"""def removing_falsy_values():
    a = input("enter the values (comma separated): ").split(",")
    # Remove common falsy string representations and empty strings
    falsy_values = {"0", "false", "", "null", "undefined", "NaN"}
    filtered = [i for i in a if i.strip().lower() not in falsy_values]
    print(filtered) 
removing_falsy_values()"""

# printing only unique numbers
"""def unique_once_elements():
    a = input("Enter the numbers (comma separated): ").split(",")
    numbers = [int(i) for i in a]
    unique_once = [x for x in numbers if numbers.count(x) == 1]
    print("Elements that appear only once:", unique_once)

unique_once_elements()"""

#printing the sum of the even numbers in a array
"""def sum_of_even_numbers():
    a = input("enter the numbers:").split(",")
    numbers = [int(i) for i in a]
    evennumb = [x for x in numbers if x % 2 == 0]
    sum_even = sum(evennumb)
    print(sum_even)
sum_of_even_numbers()"""

#reverse of a string
"""def reverse_of_string(s):
    return s[::-1]
a = input("enter the string:")
result = reverse_of_string(a)
print(result)"""

#string is a palendrome
"""def string_is_palindrome(s):
    return s[::-1]
a = input("enter the string value:")
result = string_is_palindrome(a)
if result == a:
    print(True)
else:
    print(False)"""

# printing the number of vowels in astring
"""def number_of_string():
    a = input("enter the string value:")
    b = a.lower()
    count_a = b.count('a')
    count_e = b.count('e')
    count_i = b.count('i')
    count_o = b.count('o')
    count_u = b.count('u')
    print(count_a + count_e + count_i + count_o + count_u)
number_of_string()"""

"""def count_vowels():
    s = input("Enter the string value: ").lower()
    count = sum(1 for ch in s if ch in "aeiou")
    print(count)

count_vowels()"""

#removing the vowel for the string using function
"""def remove_vowel():
    s = input("enter the string value:").lower()
    no_vowels = ''.join(ch for ch in s if ch not in "aeiou")
    print(no_vowels)
remove_vowel()

              (or)

def remove_vowel():
    s = input("enter the string value:").lower()
    no_vowels = ''.join([ch for ch in s if ch not in "aeiou"])
    print(no_vowels)
remove_vowel()"""

#Convert String to Title Case
"""def string_to_title_case(s):
    return s.title()
a = input("enter the string value:")
result = string_to_title_case(a)
print(result)
"""

#converting the string to the number
"""def string_to_number(s):
    num = 0
    for ch in s:
        digit = ord(ch) - ord('0')
        num = num*10+digit
    return num
s = input("Enter the string:")
print(string_to_number(s))"""

#checking the given string is having only digits
"""def checking_digits(s):
    return s.isdigit()
a = input("enter the string value:")
result = checking_digits(a)
print(result)
"""

#counting the occurrence of a character in the string function
"""def count_occurrence(s):
    ch = input("Enter the character to count: ")
    count = s.count(ch)
    return count

a = input("Enter the string: ")
result = count_occurrence(a)
print(result)"""

#converting an array to object using dictionary function
"""def array_to_object():
    raw_input = input("Enter key-value pairs (example: [['name', 'Alice'], ['age', 25]]): ")
    data = eval(raw_input)  
    answer = dict(data)
    return answer

result = array_to_object()
print(result)"""

# merging the two objects using def function
"""def merge_objects(obj1, obj2):
    merged = obj1.copy()   # Make a copy so original is not changed
    merged.update(obj2)    # Merge: obj2 values overwrite obj1 if same keys
    return merged

# Test case
a = {'a': 1, 'b': 2}
b = {'b': 3, 'c': 4}

result = merge_objects(a, b)
print(result)
"""
"""                 (or)
def merge_objects(obj1, obj2):
    merged = obj1.copy()   # Make a copy so original is not changed
    merged.update(obj2)    # Merge: obj2 values overwrite obj1 if same keys
    return merged

# Take input from user
a = eval(input("Enter the first object (e.g. {'a': 1, 'b': 2}): "))
b = eval(input("Enter the second object (e.g. {'b': 3, 'c': 4}): "))

# Merge and print result
result = merge_objects(a, b)
print("Merged object:", result)"""

#counting the number of properties in the given object
"""def count_of_object(obj):
    return len(obj)
a = eval(input("enter the object:"))
result = count_of_object(a)
print(result)"""

# To print all the key's in the gien array
"""def all_keys(obj):
    return obj.keys()
a = eval(input("enter the object:"))
result = all_keys(a)
print(result)"""

# to print the object values in the given object
"""def all_keys(obj):
    return obj.values()
a = eval(input("enter the object:"))
result = all_keys(a)
print(result)"""

#checking the given on=bject is empy ot not
"""def object_empty(obj):
    return len(obj) == 0
a = eval(input("enter the object:"))
result = object_empty(a)
print(result)"""


"""def is_Palindrome(x):
    return x[::-1]
a = input("enter the value of x:")
result =  is_Palindrome(a)
if result == a:
    print(True)
else:
    print(False)"""

##MATCH statement in the python
"""def week_day(obj):
    return(obj)
a = input("enter the input value:")
match a:
    case"1":
        print("Monday")
    case"2":
        print("Tuesday")
    case"3":
        print("Wednesday")
    case"4":
        print("Thursday")
    case"5":
        print("Friday")
    case"6":
        print("Saturday")
    case"7":
        print("Sunday")     
week_day(a)  
"""
#FIZZ Question
"""def FizzBuzz(n):
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            print("Fizz")
"""

#printing the name of the details using the input
"""a = input("enter the name:")
b = input("enter the age:")
c = input("enter the cgpa:")
e = int(b)
f = float(c)
g = input("enter the grade:")
print(f"Name:{a}\nage:{e}\ncgpa:{f}\nGrade:{g}")"""
        
#Input & Output - Gym Membership Registration System
"""a = input("Enter the name: ")
print("Select the plan:\n1. Monthly\n2. Yearly")
plan_choice = input("Enter 1 for Monthly or 2 for Yearly: ")
if plan_choice == "1":
    b = "Monthly"
elif plan_choice == "2":
    b = "Yearly"
else:
    b = "Invalid selection"
print(f"Member Name: {a}\nMembership plan: {b}")"""

# text-based adventure game.
"""def display_intro():
    print("Welcome to the Mysterious Forest!")
    print("You find yourself at the edge of a dark and ancient woods.")
    print("Your goal is to find the hidden treasure.")
    print("Type 'help' for available commands.")

def show_help():
    print("\nAvailable commands:")
    print("  go [north/south/east/west] - Move in a direction")
    print("  look - Describe your current surroundings")
    print("  inventory - Check your items")
    print("  take [item] - Pick up an item")
    print("  use [item] - Use an item")
    print("  quit - Exit the game")

def main():
    current_room = "forest_edge"
    inventory = []
    game_over = False

    rooms = {
        "forest_edge": {
            "description": "You are at the edge of the forest. To the north, a winding path leads deeper into the trees. To the east, you hear the faint sound of a river.",
            "exits": {"north": "winding_path", "east": "riverbank"},
            "items": ["old map"]
        },
        "winding_path": {
            "description": "The path is overgrown, with ancient trees towering above. You see a glimmering object in the distance.",
            "exits": {"south": "forest_edge", "north": "clearing"},
            "items": ["shiny key"]
        },
        "riverbank": {
            "description": "A calm river flows gently. A small, rickety bridge spans the water to the west.",
            "exits": {"west": "forest_edge", "north": "old_mill"},
            "items": []
        },
        "clearing": {
            "description": "You've reached a small clearing with a mysterious pedestal in the center.",
            "exits": {"south": "winding_path"},
            "items": []
        },
        "old_mill": {
            "description": "An abandoned mill stands silently. A locked chest sits in the corner.",
            "exits": {"south": "riverbank"},
            "items": ["locked chest"]
        }
    }

    display_intro()

    while not game_over:
        print(f"\n--- You are in the {current_room.replace('_', ' ').title()} ---")
        print(rooms[current_room]["description"])

        command = input("> ").lower().split()

        if not command:
            continue

        action = command[0]
        argument = " ".join(command[1:]) if len(command) > 1 else ""

        if action == "quit":
            game_over = True
            print("Thanks for playing!")
        elif action == "help":
            show_help()
        elif action == "go":
            if argument in rooms[current_room]["exits"]:
                current_room = rooms[current_room]["exits"][argument]
            else:
                print("You can't go that way.")
        elif action == "look":
            if rooms[current_room]["items"]:
                print("You see:", ", ".join(rooms[current_room]["items"]))
            else:
                print("There are no notable items here.")
        elif action == "take":
            if argument in rooms[current_room]["items"]:
                inventory.append(argument)
                rooms[current_room]["items"].remove(argument)
                print(f"You took the {argument}.")
            else:
                print("That item is not here.")
        elif action == "inventory":
            if inventory:
                print("Your inventory:", ", ".join(inventory))
            else:
                print("Your inventory is empty.")
        elif action == "use":
            if argument == "shiny key" and current_room == "old_mill" and "locked chest" in rooms[current_room]["items"]:
                if "shiny key" in inventory:
                    print("You unlocked the chest! Inside, you find the legendary treasure!")
                    game_over = True
                else:
                    print("You don't have the key.")
            else:
                print("You can't use that here or in that way.")
        else:
            print("Invalid command. Type 'help' for assistance.")

if __name__ == "__main__": 

    main()"""


##Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

#Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
"""def roman_to_int(s):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    for char in reversed(s.upper()):
        value = roman_dict.get(char, 0)
        if value < prev_value:
            total -= value
        else:
            total += value
            prev_value = value
    return total if total > 0 else None

b = input("Enter your Roman Numerals: ")
result = roman_to_int(b)
if result:
    print(result)
else:
    print("Invalid Roman numeral")
"""

# a = input("Enter the starting number: ")
# b = input("Enter the ending number: ")
# c = int(a)
# d = int(b)
# primes = []
# for num in range(c, d + 1):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             primes.append(num)
# print("Prime numbers:", primes)
# If you want as a comma-separated string:
#print("Prime numbers:", ', '.join(map(str, primes)))

# def is_primes(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# start = int(input("Enter the starting number: "))
# end = int(input("Enter the ending number: "))
# primes = [str(i) for i in range(start, end + 1) if is_primes(i)]
# print("Prime numbers:", ', '.join(primes))


##
"""a = ["flower","flow","flight"]
min_length = min(len(word) for word in a)
prefix = ""
for i in range(min_length):
    current_char = a[0][i]
    if all(word[i] == current_char for word in a):
        prefix += current_char
    else:
        break
print("Longest common prefix:", prefix)"""

## disaster management assigning teams to the effected zones
"""class disaster_zones():
    def __init__(self,zoneID,severnity,population,resource_shortage):
        self.zoneid = zoneID
        self.severnity = severnity
        self.population = population
        self.resource_shortage = resource_shortage
        self.priority = self.calculating_priority()

    def calculating_priority(self):
        self.score = self.severnity*self.population
        if self.resource_shortage == True:
            score *= 2
            return score

class available_teams():
    def __init__(self,teamID,specialization,available):
       self.teamID = teamID
       self.specialization = specialization
       self.available = available

    def assign_teams(zones,teams):
        zones.sort(key=lambda z: z.priority,reverse =True)
        available_teams = [team for team in teams if team.available]
        print("__Team Assignments___")
        for zone in zones:
            if available_teams:
                team = available_teams.pop(0)
                print("Team{team.teamID} [{team.specialization}] assigned to {zone.zoneID}")
            else:
                print(f"No available team for zone {zone.zoneID}")
z = int(input("enter the value:"))
zones = []
for _ in range(z):
    parts = input().split()
    zoneID = parts[0]
    severity = int(parts[1])
    population = int(parts[2])
    resourceShortage = parts[3].lower() == 'true'
    zones.append(DisasterZone(zoneID, severity, population, resourceShortage))

t = int(input())
teams = []
for _ in range(t):
    parts = input().split()
    teamID = parts[0]
    specialization = parts[1]
    available = parts[2].lower() == 'true'
    teams.append(ResponseTeam(teamID, specialization, available))

assign_teams(zones, teams)
"""

## checking the given input is a valid parenthesis or not
"""from unittest import result


class solution:
    def valid_parenthesis(s):
        empty = []
        valid_brackets = {'(':')','{':'}','[':']'}
        for bracket in s:
            if bracket in valid_brackets:
                empty.append(bracket)
            elif not empty or valid_brackets[empty.pop()] != bracket:
                return False
        return len(empty) == 0
    s  = input ("enter the parenthesis:")
    result = valid_parenthesis(s)
    print (result)"""

##OOPS CONCEPTS PRACTICE PROBLEMS
#ABSTRACTION
# ENCAPSULATION
# INHERITANCE
# POLYMORPHISM
# 🔹 LEVEL 1: Basics of OOP (Class & Object)
# 1️⃣ Student Class

# Create a class Student with:

# attributes: name, roll_no, marks

# method display() to print student details

# 👉 Create 2 objects and display their data.

"""class Student:
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks
    def display(self):
        print(f"name:{self.name}\n roll_no:{self.roll}\n marks:{self.marks}")
s1 = Student("pavan","23102A010664",98)
s2 = Student("siva","23102A010665",85)
s1.display()
s2.display()"""

# 2️⃣ Rectangle Area

# Create a class Rectangle with:

# attributes: length, width

# method area() → returns area

# method perimeter()

"""class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

r1 = rectangle(5, 3)
print("Area", r1.area())
print("Perimeter", r1.perimeter())
"""
# 3️⃣ Bank Account (Basic)

# Create a class BankAccount with:

# attributes: account_no, holder_name, balance

# methods:

# deposit(amount)

# withdraw(amount)

# check_balance()

"""class Bankaccount:
    def __init__(self,account_no,holder_name,balance):
     self.account_no = account_no
     self.holder_name = holder_name
     self.balance = balance
   
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self,amount):
        self.balance -= amount
        return self.balance
    def check_balance(self):
         return self.balance

customer1 = Bankaccount("23102A010664","GPSK",100000)
print(f"deposited_amount:{customer1.deposit(100000)}")
print(f"balance status:{customer1.check_balance()}")
print(f"withdrawn_amount:{customer1.withdraw(50000)}")
"""

# 🔹 LEVEL 2: Constructor (__init__) & Instance Methods
# 4️⃣ Employee Salary

# Create a class Employee:

# attributes: emp_id, name, basic_salary

# method calculate_salary()
# (HRA = 20%, DA = 10%)

"""class employee:
   
    def __init__(self,emp_id,name,b_salary):
        
        self.emp_id = emp_id
        self.name = name
        self.b_salary = b_salary
    def calculate_salary(self):
        HRA = self.b_salary*20/100
        DA = self.b_salary*10/100
        Total_salary = self.b_salary+HRA+DA
        return Total_salary

emp1 = employee(664,"pavan_siva_krishna",100000)
print(emp1.calculate_salary()) """

# 5️⃣ Car Details

# Create a class Car:

# attributes initialized using constructor

# method get_car_info()

"""class car:
  
   def __init__(self,company,model,capacity):
      
       self.company = company
       self.model = model
       self.capacity = capacity
        
   def get_car_details(self):
     return (f"company:{self.company}\nmodel:{self.model},\ncapacity:{self.capacity}")


car1 = car("mercedes_Benz","G-VAGAN","5-seater")
car2 = car("volvo","volvo_M-class","4-seater")
print(car1.get_car_details())
print(car2.get_car_details())
"""

# 🔹 LEVEL 3: Encapsulation (Private Variables)
# 6️⃣ Secure Bank Account

# Create a class BankAccount with:

# private variable __balance

# methods:

# deposit()

# withdraw()

# get_balance()

# ❗ Prevent direct access to balance

"""class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Withdrawn:", amount)

    def get_balance(self):
        return self.__balance
account = BankAccount(10000)

account.deposit(5000)
account.withdraw(3000)

print("Current Balance:", account.get_balance())"""


# 7️⃣ Password Protection

# Create a class User with:

# private variable __password

# method check_password(input_password)

"""class user:
    def __init__ (self,password):
        self.__password = password

    def check_password(self,input_password):
        if input_password == self.__password:
            return True
        else:
            return False
user1 = user("gpsK@2005")
print(user1.check_password("gpsK@2005")) 
print(user1.check_password("wrong_password"))
"""

#INHERITANCE
# INHERITANCE MEANS child class uses the parent class 
# there 3 types of inheritances
# single inheritance (partnt --> child)
# multilevel inheritance (prent --> child --> grandchild)
# hierachieal inheritance (single parent --> 2 or more child)

