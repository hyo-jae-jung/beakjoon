import sys
from collections import deque

N = int(sys.stdin.readline().strip())
A = list(map(int,sys.stdin.readline().strip().split()))

def carc(A:list):
    answer = 0
    A = deque(sorted(A,reverse=True))
    AA = deque()
    i=0
    while A:
        if i%2 == 0:
            AA.append(A.popleft())
        else:
            AA.append(A.pop())
        i+=1

    for i in range(len(AA)-1):
        answer+=abs(AA[i]-AA[i+1])

    return answer

if __name__ == "__main__":
    print(carc(A))
