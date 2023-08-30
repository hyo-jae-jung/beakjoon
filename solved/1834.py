from sys import stdin 

N = int(stdin.readline().strip())
arr = []
i = 1
while True:
    tmp = i*(N+1)
    if (tmp)//N == (tmp)%N:
        arr.append(tmp)
        i+=1
    else:
        print(sum(arr))
        break
