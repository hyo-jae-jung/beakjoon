from sys import stdin 

N,L = [int(i) for i in stdin.readline().strip().split()]

answer = []

while L <= 100:
    temp = N/L-L/2+0.5
    if temp >= 0 and temp == int(temp):
        for i in range(L):
            answer.append(int(temp+i))
        break
    else:
        L+=1
else:
    answer.append(-1)

print(*answer)
