from sys import stdin   

ans = []
t0 = float(stdin.readline().strip())
while (t:=float(stdin.readline().strip())) != 999:
    ans.append(f"{t-t0:.2f}")
    t0 = t
print(*ans,sep='\n')
