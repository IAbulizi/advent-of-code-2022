import numpy as np

def read_file(filename, verbose = False):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    if verbose:
        print(f"Read file, print first 5 lines:\n{lines[:10]}")
    return lines

def get_max_day8(arr):
    try:
        return np.max(arr)
    except ValueError:
        return -1