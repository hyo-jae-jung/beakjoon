import sys

N = int(sys.stdin.readline().strip())
answer = 0
i=0
while N>9*(10**i):
    answer+=(i+1)*9*(10**i)
    N-=9*(10**i)
    i+=1
else:
    answer+=N*(i+1)

print(answer)
