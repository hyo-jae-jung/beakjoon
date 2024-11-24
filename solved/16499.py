from sys import stdin  

N = int(stdin.readline().strip())
ans = set()
for _ in range(N):
    s = stdin.readline().strip()
    b = [0]*26
    for i in s:
        b[ord(i)-97]+=1
    
    ans.add("".join(map(str,b)))

print(len(ans))
