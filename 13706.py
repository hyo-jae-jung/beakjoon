from sys import stdin 
N = int(stdin.readline().strip())
s = [1,1,0]
i = 2
while N > 1:
    if N%i == 0:
        s[i]+=1
        N = N//i
    else:
        s.append(0)
        i+=1

answer = 1
for i,j in enumerate(s[2:],2):
    if j:
        answer*=i**(j//2)

print(answer)
    