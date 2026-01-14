"""File handling with exception handling examples."""


def safe_read(path: str):
    try:
        return open(path, 'r', encoding='utf-8').read()
    except FileNotFoundError:
        return None


# Practice (5):
# 1) Use try/except with file IO.
# 2) Ensure files are closed even when exceptions occur.
# 3) Retry on transient IO errors with backoff.
# 4) Validate file permissions before writing.
# 5) Sanitize file paths to prevent path traversal.

if __name__ == "__main__":
    print(safe_read('nonexistent.txt'))
    # example: retry template
    import time
    def retry_read(path, retries=3):
        for i in range(retries):
            try:
                return open(path).read()
            except Exception as e:
                time.sleep(0.1)
        return None
