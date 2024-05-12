from sys import stdin  

m,n = map(int,stdin.readline().strip().split())
d = {}
for i in range(17):
    if i < 10:
        d.update({i:str(i)})
    else:
        d.update({i:chr(i+55)})
ans = ''

while m%n > 0 or m >= n:
    ans = d[m%n] + ans
    m = m//n

print(ans if ans else 0)
