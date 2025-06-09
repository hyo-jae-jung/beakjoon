from sys import stdin  

N = int(stdin.readline().strip())
ans = []
for _ in range(N):
    arr = sorted(list(map(int,stdin.readline().strip().split()))[1:])
    brr = sorted(list(map(int,stdin.readline().strip().split()))[1:])

    while True:
        A = arr.pop()
        B = brr.pop()

        if A > B:
            ans.append('A')
            break
        elif A < B:
            ans.append('B')
            break

        if not arr and brr:
            ans.append('B')
            break
        elif arr and not brr:
            ans.append('A')
            break
        elif not arr and not brr:
            ans.append('D')
            break

print(*ans,sep='\n')

