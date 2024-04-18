from sys import stdin 

N = int(stdin.readline().strip())
ans = []
for _ in range(N):
    front,end = stdin.readline().strip().split('-')
    front_decode = 0
    for i,j in zip(range(len(front)-1,-1,-1),front):
        front_decode+=(ord(j)-65)*(26**i)

    end_decode = int(end)
    
    ans.append('nice' if abs(front_decode-end_decode) <= 100 else 'not nice')

print(*ans,sep='\n')
