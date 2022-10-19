import sys

N = int(sys.stdin.readline().strip())

def fibonacci(number:int):
    if number == 0:
        return 0
    elif number == 1:
        return 1        
    return fibonacci(number-1) + fibonacci(number-2)

print(fibonacci(N))