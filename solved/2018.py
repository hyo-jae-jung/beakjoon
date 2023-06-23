from sys import stdin 

N = int(stdin.readline().strip())

def accum_sum(n):
    return n*(n+1)//2

answer = 0
i,j = 0,1
while i<j:
    temp = accum_sum(j)-accum_sum(i)
    if temp < N:
        j+=1
    else:
        i+=1
        if temp == N:
            answer+=1

print(answer)
