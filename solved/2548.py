from sys import stdin 

N = int(stdin.readline().strip())
A = [int(i) for i in stdin.readline().strip().split()]

d = {}
for i in A:
    if not d.get(i):
        d.update({i:0})
    d[i]+=1

val = max(A)*len(A)+1
for i in range(1,max(A)+1):
    tmp = 0
    for num,cnt in d.items():
        tmp+=abs(num-i)*cnt
    if tmp < val:
        ans = i 
        val = tmp
    elif tmp >= val:
        break

print(ans)
