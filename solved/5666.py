from sys import stdin  

ans = []
while s:=stdin.readline().strip():
    H,P = map(int,s.split())
    ans.append(H/P)

for i in ans:
    print(f"{i:.2f}")
