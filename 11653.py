N = int(input())

if N != 1:
    division_number = 2
    while N != 1:
        while N%division_number == 0:
            print(division_number)
            N = N//division_number
        division_number += 1
