def read_file(filename, verbose = False):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    if verbose:
        print(f"Read file, print first 5 lines:\n{lines[:10]}")
    return lines