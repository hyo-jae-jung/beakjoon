from sys import stdin 

N = int(stdin.readline().strip())

i = 1

while True:
    N-=i
    i+=1
    if N < i:
        if i%2 == 1:
            print(i-N)
        else:
            print(0)
        break

