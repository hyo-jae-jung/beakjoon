from sys import stdin   

_ = stdin.readline().strip()
name = stdin.readline().strip()

ans = 0

for i in name:
    ans+=(ord(i) - 64)

print(ans)
