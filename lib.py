def read_file(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    print(f"Read file, print first 5 lines:\n{lines[:10]}")
    return lines