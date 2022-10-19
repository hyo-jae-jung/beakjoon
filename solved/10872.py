import sys

N = int(sys.stdin.readline().strip())

def factorial(number:int):
    if number == 0:
        return 1
    else:
        if number == 1:
            return 1
    return number * factorial(number-1)

print(factorial(N))