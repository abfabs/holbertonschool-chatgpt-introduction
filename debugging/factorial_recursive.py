#!/usr/bin/python3
import sys

def factorial(n):
    """Function Description:
    Compute the factorial of a non-negative integer using a recursive approach.

    Parameters:
        n (int): A non-negative integer whose factorial will be computed.

    Returns:
        int: The factorial of n. For n == 0, returns 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

f = factorial(int(sys.argv[1]))
print(f)
