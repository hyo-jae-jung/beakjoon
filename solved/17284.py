from sys import stdin  

ans = 5000
d = {'1':500,'2':800,'3':1000}
for i in stdin.readline().strip().split():
    ans-=d[i]

print(ans)
