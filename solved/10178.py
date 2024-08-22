from sys import stdin  

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    c,v = map(int,stdin.readline().strip().split())
    ans.append(f"You get {c//v} piece(s) and your dad gets {c%v} piece(s).")

print(*ans,sep='\n')
