"""Examples for tuple usage"""


def swap_in_tuple(tpl, i, j):
    lst = list(tpl)
    lst[i], lst[j] = lst[j], lst[i]
    return tuple(lst)


# Practice (5):
# 1) Use tuple unpacking to swap values.
# 2) When to use tuple vs list (immutability trade-offs).
# 3) Use tuples as dict keys and explain why.
# 4) Convert list of tuples to dict and back.
# 5) Implement nested tuple traversal and flattening.

if __name__ == "__main__":
    print(swap_in_tuple((1,2,3), 0, 2))
    print('as key', {('a','b'): 1})
