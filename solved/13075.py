from sys import stdin  

t = int(stdin.readline().strip())
ans = []

def metrix_multi(A,B):

    new = [[0,0],[0,0]]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                new[i][j]+=A[i][k]*B[k][j]%(10**9)

    return new


def get_nth(n):

    elementary_metrix = [[1,0],[0,1]]
    fibonacci_metrix = [[1,1],[1,0]]

    while n > 0:
        if n%2 == 1:
            elementary_metrix = metrix_multi(elementary_metrix,fibonacci_metrix)
        n//=2
        fibonacci_metrix = metrix_multi(fibonacci_metrix,fibonacci_metrix)

    return elementary_metrix[1][0]%(10**9)

for _ in range(t):
    x = int(stdin.readline().strip())
    ans.append(get_nth(x))

print(*ans,sep='\n')
