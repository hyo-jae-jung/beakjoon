from sys import stdin  

N = int(stdin.readline().strip())
arr = []
for _ in range(N):
    arr.append(sum(map(int,stdin.readline().strip().split()[1:])))

ans = 0
arr_s = sorted(arr)
accum = [arr_s[0]]
for i in range(1,len(arr_s)):
    accum.append(arr_s[i]+accum[-1])

print(sum(accum))

