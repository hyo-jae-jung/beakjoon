from sys import stdin   

N,L,R,X = map(int,stdin.readline().strip().split())
A = list(map(int,stdin.readline().strip().split()))

ans = 0

def solution(cnt=0,total=0,l=float('inf'),r=-float('inf'),idx=0):
    global ans,N,L,R,X 

    if total > R:
        return 

    if cnt >= 2 and L <= total <= R and r-l >= X:
        ans+=1


    for i in range(idx,N):
        solution(cnt+1,total+A[i],l=min(l,A[i]),r=max(r,A[i]),idx=i+1)

solution()
print(ans)
