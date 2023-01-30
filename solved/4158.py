from sys import stdin 
from collections import deque 

answer = []
while True:
    N,M = map(int,stdin.readline().strip().split())

    if N == 0 and M == 0:
        break

    sanggun = deque()
    sunyoung = deque()

    for _ in range(N):
        sanggun.append(int(stdin.readline().strip()))

    for _ in range(M):
        sunyoung.append(int(stdin.readline().strip()))

    temp_sun,temp_sang = '',''

    answer.append(len(set(sanggun) & set(sunyoung)))

if answer:
    print(*answer, sep='\n')
