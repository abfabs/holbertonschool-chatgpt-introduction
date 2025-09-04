#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("n must be >= 0")
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <non-negative-integer>")
        sys.exit(1)
    n = int(sys.argv[1])
    print(factorial(n))
