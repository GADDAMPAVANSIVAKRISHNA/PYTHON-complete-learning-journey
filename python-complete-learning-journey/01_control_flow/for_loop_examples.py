"""For loop examples and practice problems"""


def sum_list(nums):
    total = 0
    for n in nums:
        total += n
    return total


# Practice (5):
# 1) Use a for loop to flatten a list of lists.
# 2) Implement a function that returns frequency count using a loop.
# 3) Use enumerate to find indices of matching items.
# 4) Iterate over two lists in parallel with zip and handle unequal lengths.
# 5) Use a loop to implement sliding window maximum of size k.

# Sample solution for 1 and 2:
def flatten(l):
    out=[]
    for sub in l:
        for x in sub:
            out.append(x)
    return out

def freq(lst):
    d={}
    for x in lst:
        d[x]=d.get(x,0)+1
    return d

if __name__ == "__main__":
    print(sum_list([1,2,3,4]))
    print(flatten([[1,2],[3]]), freq([1,2,1]))
