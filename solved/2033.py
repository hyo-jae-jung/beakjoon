from sys import stdin 

N = int(stdin.readline().strip())

criteria = 10
while criteria < N:
    c = N%criteria//(criteria//10)
    if c >= 5:
        N+=criteria
    N = N//criteria*criteria
    criteria*=10

print(N)
