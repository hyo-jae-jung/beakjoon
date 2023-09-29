from sys import stdin 

U = list(map(int,stdin.readline().strip().split()))
S = list(map(int,stdin.readline().strip().split()))

winning = False
total_score_diff = 0

for i,j in zip(U,S):
    total_score_diff+=i
    if (not winning) and (total_score_diff > 0):
        winning = True
    total_score_diff-=j
else:
    lose = True if total_score_diff < 0 else False

print('Yes' if (winning and lose) else 'No')
