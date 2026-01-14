"""Nested conditions examples"""


def grade(score: int) -> str:
    if score >= 90:
        return 'A'
    else:
        if score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        else:
            return 'F'


# Practice (5):
# 1) Use nested conditions to check triangle validity and type.
# 2) Implement nested discounts based on membership and cart value.
# 3) Nested decision for tax brackets based on income and status.
# 4) Validate nested dict inputs (user->address->zip) with conditions.
# 5) Implement availability checks that nest product and stock rules.

# Sample solution for 1:
def triangle_type(a,b,c):
    if a+b<=c or a+c<=b or b+c<=a:
        return 'invalid'
    if a==b==c:
        return 'equilateral'
    if a==b or b==c or a==c:
        return 'isosceles'
    return 'scalene' 