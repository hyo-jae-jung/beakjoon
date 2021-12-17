import sys

N = int(sys.stdin.readline().strip())

def stars(number:int):
    if number == 1:
        sys.stdout.write('*')

    elif number == 3:
        for i in range(number):
            for j in range(number):
                if j%3 == 1:

# fail...