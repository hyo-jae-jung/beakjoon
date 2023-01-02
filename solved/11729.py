from sys import stdin

N = int(stdin.readline().strip())

arr = []
def hanoi(n, start, end, stopover):
    if n == 1:
        arr.append([start,end])
    else:
        hanoi(n-1, start, stopover, end)
        arr.append([start,end])
        hanoi(n-1, stopover, end, start)

hanoi(N,1,3,2)
print(len(arr))
for i in arr:
    print(*i)
