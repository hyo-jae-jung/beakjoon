from sys import stdin 

N = int(stdin.readline().strip())
A = list(map(int,stdin.readline().strip().split()))

def check_seq_type(l:list)->bool:
    if len(l) < 3:
        return True
    else:
        diff = l[1] - l[0]
        for i in range(2,len(l)):
            if l[i] - l[i-1] != diff:
                return False
        else:
            return True
            
if check_seq_type(A):
    print('YES')
    print(*A)
    print(*[0]*N)
else:
    print('NO')
