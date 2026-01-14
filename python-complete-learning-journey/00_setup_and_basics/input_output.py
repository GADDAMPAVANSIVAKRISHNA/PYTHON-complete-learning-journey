"""Examples for input/output and practice problems

Practice (5):
1) Parse a CSV string from input into list of lists.
2) Format a table of data into aligned columns.
3) Read lines until a sentinel value and return parsed list.
4) Implement a simple REPL that accepts commands and returns results.
5) Read and write JSON from/to files with proper encoding.

Sample solutions (examples):

def read_numbers_from_input():
    nums = input("Enter numbers separated by space: ").split()
    return [int(n) for n in nums]


def format_output(name: str, score: float) -> str:
    return f"Student {name} scored {score:.2f}"

# Example for 2 (aligned columns):
def format_table(rows):
    cols = list(zip(*rows))
    widths = [max(len(str(x)) for x in c) for c in cols]
    lines = []
    for r in rows:
        lines.append(' | '.join(str(v).ljust(w) for v, w in zip(r, widths)))
    return '\n'.join(lines)

if __name__ == "__main__":
    # simple demo
    print(format_output('Alice', 92.3456))
    print(format_table([['Name','Score'],['Bob',90],['Ann',100]]))
