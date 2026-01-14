## Sum of Digits
##Input a number, find the sum of its digits (using loops).
##➜ Concepts: Loops, integer operations

"""a = int(input("Enter a number: "))
if a == 0:
 print(False)
else:
 total = 0
for digit in str(a):
  total += int(digit)
print(total)"""

##Count Vowels in a String
##Take a string and count vowels (a, e, i, o, u).
##➜ Concepts: Strings, loops, conditions

"""a = input("Enter the string: ")
b = a.lower()
vowels = "aeiou"
count = 0
for ch in b:
  if ch in vowels:
    count += 1
print(count if count > 0 else False)"""

# Check Palindrome (Number/String)
# Determine if a number or string is palindrome.
# ➜ Concepts: String slicing, condition
"""a = input("Enter the string/Number:")
if a == a[::-1]:
    print(True)
else :
    print(False)"""

# Find Maximum of Three Numbers
# Without using max().
# ➜ Concepts: If-else logic
"""s = input("Enter three numbers separated by commas: ")
parts = [p.strip() for p in s.split(',') if p.strip() != '']
if len(parts) < 3:
  print("Please enter three numbers")
else:
  try:
    a, b, c = (int(parts[0]), int(parts[1]), int(parts[2]))
  except ValueError:
    print("Invalid integer input")
  else:
    if a >= b and a >= c:
      print(a)
    elif b >= a and b >= c:
      print(b)
    else:
      print(c)"""


# Fibonacci Series up to N
# Print first N Fibonacci numbers.
# ➜ Concepts: Loops, sequence generation
"""n = int(input("Enter N: "))
a, b = 0, 1
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b"""

# LEVEL 2 – Data Structure Logic (Core Thinking)
# List Operations
# Given a list of numbers, remove duplicates, sort it, and print the 2nd largest number.
# ➜ Concepts: Lists, sets, sorting
#lists
"""a = input("Enter the list of numbers:").split(",")
if len(a)<2:
    print("List should be of at least two numbers")
else:
    b = []
    for num in a:
        if num not in b:
            b.append(num)
b.sort()
print(b[-1])"""

# Dictionary Word Count
# Count frequency of each word in a sentence.
# ➜ Concepts: Dictionaries, loops, string split
"""a = input("Enter a sentence:")
words = a.split()
for word in set(words):
    print("frequency of",word,"is:",words.count(word))
    """

# Find Common Elements
# Between two lists or sets.
# ➜ Concepts: Sets, intersections
"""a = input("Enter the first list of numbers:").split(",")
b = input("Enter the second list of nubers:").split(",")
set_a = set(a)
set_b =set(b)
common_elements = set_a.intersection(set_b)
print("common elements are:",common_elements)"""

# Tuple Unpacking Problem
# Given a list of tuples (name, age), print names of people older than 18.
# ➜ Concepts: Tuples, iteration
"""a = [("Alice",17),("Bob",20),("charlie",19),("David",16)]
for name,age in a:
    if age>18:
        print(name)"""

# Matrix Diagonal Sum
# Calculate the sum of both diagonals of a square matrix.
# ➜ Concepts: Nested loops, indexing
"""matrix = [
    [1,2,3],
    [2,4,5],
    [3,6,7]
]
n = len(matrix)
first_diagonal_sum = 0
second_diagonal_sum = 0
for i in range(n):
    first_diagonal_sum += matrix[i][i]
    second_diagonal_sum += matrix[i][n-i-1]
    total_sum = first_diagonal_sum + second_diagonal_sum
print(total_sum)"""


# LEVEL 3 – OOP, File, Regex, JSON, Exception Handling

# Student Class Problem
# Create a Student class with name, marks, and method to find grade.
# ➜ Concepts: Class, __init__, methods
"""class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        elif self.marks >= 60:
            return "D"
        else:
            return "F"
s1 = student("pavan",98)
s2 = student("venkat",85)
print("student_details:")
print(s1.name,s1.marks,s1.grade())
print(s2.name,s2.marks,s2.grade())"""

# File Handling – Word Counter
# Read a text file and count number of lines, words, and characters.
# ➜ Concepts: File I/O, loops
"""try:
    with open("C:/Users/gpskr/Downloads/Niharika_Resume.pdf", "rb") as file:
        content = file.readlines()
        line_count = len(content)
        word_count = sum(len(line.split()) for line in content)
        char_count = sum(len(line) for line in content)
    print("Lines:",line_count)
    print("Words:",word_count)
    print("Characters:",char_count)
except FileNotFoundError:
    print("File not found.")
"""

#amother methos of file handling – Word Counter
"""with open("sample.txt","w") as f:
    f.write("Hello world\n")
    f.write("This is a sample file:\n")
    f.write("It contains multiple lines of text.\n")
    f.write("We will use it to demonstrate file handling in Python.\n")

lines = 0
words = 0
characters = 0
with open("sample.txt","r") as f:
    for line in f:
        lines += 1
        words += len(line.split())
        characters += len(line)
print(f"lines:{lines}\nwords:{words}\ncharacters:{characters}")"""


# Regex – Email Validator
# Take input emails and print only valid ones.
# ➜ Concepts: Regular expressions

"""import re
pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
emails = input("Enter the emails with seperate by commas").split(",")
for email in emails:
    if re.match(pattern,email):
        print(f"{email},valid")
    else:
        print(f"{email},Invalid")"""

# JSON – Convert Dictionary to JSON File
# Take a Python dictionary, convert it to JSON, and save it in a file.
# ➜ Concepts: JSON module, file writing
"""import json
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "courses": ["Math", "Science", "History"]
}
with open("data.json","w") as json_file:
    json.dump(data,json_file,indent=4)
    print("Data haas been written to data.json file")
"""

"""import json
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "courses": ["Math", "Science", "History"]
}
y = json.dumps(data)
print(y)"""


# Try-Except – Safe Division
# Ask user for two numbers and divide them safely (handle division by zero).
# ➜ Concepts: Exception handling

"""try:
    a = float(input("Enter the numerator:"))
    b = float(input("Enter the denominator:"))
    result = a / b
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
else:
    print(f"The result of {a} divided by {b} is: {result}")"""

