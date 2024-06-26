from sys import stdin  


N = int(stdin.readline().strip())
arr = []
for _ in range(N):
    arr.append(stdin.readline().strip().split())

arr.sort(key=lambda x:(int(x[1])))

ans = ''
for i,_,k in arr:
    ans+=i[int(k)-1].upper()

print(ans)
