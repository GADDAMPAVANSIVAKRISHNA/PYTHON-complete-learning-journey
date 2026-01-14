"""Append file example and practice"""


def append_line(path: str, line: str):
    with open(path, 'a', encoding='utf-8') as f:
        f.write(line + '\n')


# Practice (5):
# 1) Implement rotate logs (append then rotate when > N lines).
# 2) Use context manager for safe append.
# 3) Implement concurrent-safe append (file locking simple example).
# 4) Append JSON lines (ndjson) safely and validate JSON.
# 5) Implement log file archiving by date.

if __name__ == "__main__":
    append_line('sample_out.txt', 'another line')
    print('appended')
