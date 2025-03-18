from sys import stdin   


C = int(stdin.readline().strip())
ans = []

def count_divisor(n):
    count = 0
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            count+=1
            if i != n//i:
                count+=1
    return count

for _ in range(C):
    L,U = map(int,stdin.readline().strip().split())
    m = 0
    for i in range(L,U+1):
        m = max(m,count_divisor(i))
    ans.append(m)

print(*ans,sep='\n')
