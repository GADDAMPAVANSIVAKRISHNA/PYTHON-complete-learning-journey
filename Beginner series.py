##using match function instead of using if and else statements
day = input("Enter the day in a week:")
match day:
    case "1":
        print("Monday")
    case "2":
        print("Tuesday")
    case "3":
        print("Wednesday")
    case "4":
        print("Thursday")
    case "5":
        print("Friday")
    case "6":
        print("Saturday")
    case "7":
        print("Sunday")
try:
    day_int = int(day)
    if day_int < 1 or day_int > 7:
        print("Invalid day in a week")
except ValueError:
    print("Invalid input, please enter a number between 1 and 7.")