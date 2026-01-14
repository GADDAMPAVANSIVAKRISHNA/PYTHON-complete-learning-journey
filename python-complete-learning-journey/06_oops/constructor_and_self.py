"""Constructor and use of self"""

class Counter:
    def __init__(self):
        self.count = 0

    def inc(self):
        self.count += 1


# Practice (5):
# 1) Implement a resettable counter with `reset()`.
# 2) Demonstrate class vs instance attributes by adding `max_count` as a class attr.
# 3) Create a counter that supports ``+=`` via __iadd__.
# 4) Implement a thread-safe increment using threading.Lock.
# 5) Serialize and restore counter state to/from dict.
#
# Sample solutions (examples):
class ResetCounter(Counter):
    def reset(self):
        self.count = 0

# Example for 3 (__iadd__):
class AddCounter(Counter):
    def __iadd__(self, other):
        self.count += other
        return self

if __name__ == "__main__":
    c = ResetCounter()
    c.inc(); c.inc()
    print('before reset', c.count)
    c.reset()
    print('after reset', c.count)
    a = AddCounter(); a += 3
    print('add counter', a.count) 
