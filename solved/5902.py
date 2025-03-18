from sys import stdin   

N,L = map(int,stdin.readline().strip().split())
knots_loc = []
for _ in range(N):
    knots_loc.append(int(stdin.readline().strip()))

knots_loc.sort()
ans = 0


def solution(arr):
    i = 1
    j = len(arr)-2

    while i <= j:
        if (arr[i]-arr[i-1]) != (arr[j+1]-arr[j]):
            return 0
        i+=1
        j-=1

    return 1

i,j = 0,2
while j <= N:
    ans+=solution(knots_loc[i:j])
    j+=1
i+=1
while i < N-1:
    ans+=solution(knots_loc[i:j])
    i+=1

print(ans)
