from sys import stdin  

N = int(stdin.readline().strip())
ans = []
for _ in range(N):
    A1,P1 = map(int,stdin.readline().strip().split())
    R1,P2 = map(int,stdin.readline().strip().split())
    if A1/P1 > 3.14*R1**2/P2:
        ans.append("Slice of pizza")
    else:
        ans.append("Whole pizza")

print(*ans,sep='\n')
