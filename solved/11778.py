import sys

n,m = map(int,sys.stdin.readline().strip().split())

SIZE = 2
ZERO = [[1, 0], [0, 1]]
BASE = [[1, 1], [1, 0]]

def square_matrix_mul(a, b, size=SIZE):

     new = [[0 for _ in range(size)] for _ in range(size)]

     for i in range(size):
          for j in range(size):
               for k in range(size):
                 new[i][j] += (a[i][k] * b[k][j])%1_000_000_007

     return new

def get_nth(n):
    matrix = ZERO.copy()
    tmp = BASE.copy()

    while n > 0:
        if n % 2 == 1:
            matrix = square_matrix_mul(matrix, tmp)
        n //= 2
        tmp = square_matrix_mul(tmp, tmp)
        
    return matrix

def gcd(a,b):
    if a%b == 0:
        return b
    return gcd(b,a%b)

print(get_nth(gcd(n,m))[1][0]%1_000_000_007)
