from sys import stdin   

n = int(stdin.readline().strip())

def gcd(a,b):
    a,b = max(a,b),min(a,b)
    if a%b == 0:
        return b
    return gcd(b,a%b)

SIZE = 2
ZERO = [[1, 0], [0, 1]]
BASE = [[1, 1], [1, 0]]


def square_matrix_mul(a, b, size=SIZE):

     new = [[0 for _ in range(size)] for _ in range(size)]

     for i in range(size):
          for j in range(size):
               for k in range(size):
                 new[i][j] += (a[i][k] * b[k][j])%1_000_000_007 # 값이 크기가 커지면 계산량이 많아지기 때문에 속도에 영향을 미친다

     return new

def get_nth(n):
    matrix = ZERO.copy()
    tmp = BASE.copy()
    m_cnt = 0
    tmp_cnt = 1
    while n > 0:
        if n % 2 == 1:
            matrix = square_matrix_mul(matrix, tmp)
            m_cnt = m_cnt + tmp_cnt
            if not F.get(m_cnt):
                F.update({m_cnt:matrix[1][0]%1_000_000_007})
        n //= 2
        tmp = square_matrix_mul(tmp, tmp)
        tmp_cnt*=2

    return matrix

F = {1:1,2:1}

ans = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        val = gcd(i,j)
        if F.get(val):
            ans+=F[val]
        else:
            ans+=get_nth(val)[1][0]%1_000_000_007
print(ans)
