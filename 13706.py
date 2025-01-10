from sys import stdin 
d = {1:1,2:0}
N = int(stdin.readline().strip())
i = 2
while N > 1:
    if N%i == 0:
        if not d.get(i):
            d.update({i:0})
        d[i]+=1
        N = N//i
    else:
        i+=1

answer = 1
for key,value in d.items():
    answer*=key**(value//2)

print(answer)
    