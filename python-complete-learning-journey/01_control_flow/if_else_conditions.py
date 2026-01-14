"""If/else examples and practice questions"""

def classify_number(n: int) -> str:
    if n < 0:
        return 'negative'
    elif n == 0:
        return 'zero'
    else:
        return 'positive'


# Practice (5):
# 1) Write a function that checks whether a year is a leap year (if/else).
# 2) Classify a temperature into cold/warm/hot.
# 3) Implement grade classification with cutoffs.
# 4) Validate a simple form input (age between 0 and 120).
# 5) Use nested if to categorize triangle type by sides.

if __name__ == "__main__":
    print(classify_number(-5))
    print(classify_number(0))
    print(classify_number(7))
    # example for 3:
    def grade(score):
        return 'A' if score>=90 else 'B' if score>=80 else 'C' if score>=70 else 'F'
    print(grade(85))
