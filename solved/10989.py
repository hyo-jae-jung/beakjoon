import sys

N = int(sys.stdin.readline().strip())

count = dict()

for _ in range(N):
    temp = int(sys.stdin.readline().strip())
    if temp in count:
        count[temp]+=1
    else:
        count[temp] = 1

for i in sorted(count.keys()):
    for _ in range(count[i]):
        print(i)

    """
    메모리 초과와 시간 초과는 상대적이다.
    상황에 맞게 코드를 짜는 능력도 필요하다.
    """
    