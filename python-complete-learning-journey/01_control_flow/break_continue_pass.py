"""Examples for break, continue and pass"""


def find_first_even(nums):
    for n in nums:
        if n % 2 == 0:
            return n
    return None


# Practice (5):
# 1) Use continue to skip negative numbers while summing.
# 2) Demonstrate pass in an empty class/function placeholder.
# 3) Use break to exit nested loops when a condition is met.
# 4) Implement search that stops early with break and returns index.
# 5) Show how `else` on loops runs when loop completes normally.

if __name__ == "__main__":
    print(find_first_even([1,3,5,8,9]))
    # loop else example
    for i in range(3):
        if i==5:
            break
    else:
        print('completed without break')
