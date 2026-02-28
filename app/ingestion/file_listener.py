import time

def follow(file):
    """
    Generator that yields new lines appended to a file.
    Assumes file cursor is already positioned correctly.
    """
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.2)
            continue
        yield line