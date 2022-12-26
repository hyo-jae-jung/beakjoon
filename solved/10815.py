import sys

N = int(sys.stdin.readline().strip())
N_cards = list(map(int,sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline().strip())
M_cards = list(map(int,sys.stdin.readline().strip().split()))

answer = dict.fromkeys(M_cards,0)

intersection = set(N_cards) & set(M_cards)

for i in intersection:
    answer[i]+=1

print(*answer.values())
