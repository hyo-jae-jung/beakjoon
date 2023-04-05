import sys

answer = []
N = 101
memo = [[[0 for _ in range(N)] for _ in range(N)] for i_ in range(N)]

def w(a,b,c):
    if memo[a][b][c]:
        return memo[a][b][c]
    
    def selection(a,b,c):
        return memo[a][b][c] if memo[a][b][c] else w(a,b,c)
    
    if a <= 0 or b <= 0 or c <= 0:
        memo[a][b][c] = 1
    elif a > 20 or b > 20 or c > 20:
        memo[a][b][c] = selection(20,20,20)
    elif a < b and b < c:
        memo[a][b][c] = selection(a,b,c-1) + selection(a,b-1,c-1) - selection(a,b-1,c)
    else:
        memo[a][b][c] = selection(a-1,b,c) + selection(a-1,b-1,c) + selection(a-1,b,c-1) - selection(a-1,b-1,c-1)
        
    return memo[a][b][c]


while (ABC := sys.stdin.readline().strip()) != '-1 -1 -1':
    A,B,C = map(int,ABC.split())
    answer.append('w({}, {}, {}) = {}'.format(A,B,C,w(A,B,C)))

print(*answer,sep='\n')
