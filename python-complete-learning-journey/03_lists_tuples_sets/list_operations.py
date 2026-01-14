"""List operations and practice problems."""

def unique_preserve_order(lst):
    seen = set()
    out = []
    for x in lst:
        if x not in seen:
            out.append(x)
            seen.add(x)
    return out


# Practice (5):
# 1) Rotate a list by k steps.
# 2) Merge two sorted lists.
# 3) Remove duplicates in-place preserving order.
# 4) Implement sliding window sum for array of ints.
# 5) Partition list around a pivot (like quicksort partition).

# Sample for 1:
def rotate(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

if __name__ == "__main__":
    print(unique_preserve_order([1,2,2,3,1]))
    print('rotate', rotate([1,2,3,4], 1))
