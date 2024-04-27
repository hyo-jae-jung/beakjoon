from sys import stdin 

ans = set()

for _ in range(5):
    num = int(stdin.readline().strip())
    if num in ans:
        ans.remove(num)
    else:
        ans.add(num)

print(*ans)
