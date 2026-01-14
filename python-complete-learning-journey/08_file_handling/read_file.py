"""Reading files examples and practice."""


def read_lines(path: str):
    with open(path, 'r', encoding='utf-8') as f:
        return f.readlines()


# Practice (5):
# 1) Read a file and count word frequencies.
# 2) Read large files using streaming (generator).
# 3) Read files safely and handle encoding errors.
# 4) Read CSV files line by line and parse fields.
# 5) Implement tail -n functionality (last N lines).

# Sample for 2 (streaming):
def read_stream(path):
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            yield line

if __name__ == "__main__":
    print('Read file examples')
    print('first line via stream:', next(read_stream('README.md')) if True else '')
