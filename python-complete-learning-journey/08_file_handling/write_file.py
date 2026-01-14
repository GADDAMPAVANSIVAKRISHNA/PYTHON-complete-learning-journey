"""Writing files examples and practice."""


def write_text(path: str, text: str):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)


# Practice (5):
# 1) Append data to a CSV safely.
# 2) Write JSON data to a file.
# 3) Write atomic file updates (write to temp then rename).
# 4) Use newline handling for cross-platform writes.
# 5) Implement a backup copy before overwriting a file.

if __name__ == "__main__":
    write_text('sample_out.txt', 'Hello')
    print('written sample_out.txt')
