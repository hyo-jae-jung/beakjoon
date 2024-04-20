from sys import stdin 

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    n = int(stdin.readline().strip())
    tmp = n%28 if n%28 > 0 else 28
    ans.append(''.join(['딸기' if i == '1' else 'V' for i in bin(tmp if tmp <= 15 else abs(15-tmp%15))[2:].rjust(4,'0')]))
    
print(*ans,sep='\n')
