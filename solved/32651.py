from sys import stdin   

N = int(stdin.readline().strip())

if N > 100000:
    print('No')
elif N%2024 == 0:
    print('Yes')
elif N%2024 != 0:
    print('No')
    