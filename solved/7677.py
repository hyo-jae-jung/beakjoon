from sys import stdin  

ans = []

def metrix_multi(A,B):

    new = [[0,0],[0,0]]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                new[i][j]+=A[i][k]*B[k][j]%10000

    return new


def get_nth(n):

    matrix = [[1,0],[0,1]]
    tmp = [[1,1],[1,0]]

    while n > 0:
        if n%2 == 1:
            matrix = metrix_multi(matrix,tmp)
        n//=2
        tmp = metrix_multi(tmp,tmp)

    return matrix[1][0]

while (n:=int(stdin.readline().strip())) != -1:
    ans.append(get_nth(n)%10000)

print(*ans,sep='\n')
