import sys
from collections import deque

N,M = map(int,sys.stdin.readline().strip().split())
index_to_find = map(int,sys.stdin.readline().strip().split())
indeces = deque(range(1,N+1))
answer = 0

def left_move(x:list)->list:
    temp = x.popleft()
    x.append(temp)
    return x

def right_move(x:list)->list:
    temp = x.pop()
    x.appendleft(temp)
    return x

for i in index_to_find:
    t = indeces.index(i)
    if t <= len(indeces)-t:
        while i != indeces[0]:
            indeces = left_move(indeces)
            answer+=1
    else:
        while i != indeces[0]:
            indeces = right_move(indeces)
            answer+=1
    indeces.popleft()


if __name__ == "__main__":
    print(answer)
    