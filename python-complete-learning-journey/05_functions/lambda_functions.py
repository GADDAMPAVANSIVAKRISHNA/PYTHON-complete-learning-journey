"""Lambda function examples and exercises."""


double = lambda x: x*2


# Practice (5):
# 1) Sort a list of tuples by second element using lambda.
# 2) Combine lambda with map/filter to process data.
# 3) Use lambda for simple key functions in groupby.
# 4) Convert a list of strings to ints using map+lambda with error handling.
# 5) Use lambda to build small one-off functions in place.

if __name__ == "__main__":
    print(list(map(double, [1,2,3])))
