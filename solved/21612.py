from sys import stdin   

B = int(stdin.readline().strip())

print(ans:=5*B-400)

if ans < 100:
    print(1)
elif ans > 100:
    print(-1)
else:
    print(0)
    