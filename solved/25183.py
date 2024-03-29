from sys import stdin 

N = int(stdin.readline().strip())
S = stdin.readline().strip() 

cnt=1
for i in range(1,N):
    if ord(S[i])+1 == ord(S[i-1]) or ord(S[i])-1 == ord(S[i-1]):
        cnt+=1
    else:
        cnt = 1
    
    if cnt == 5:
        print('YES')
        break
else:
    print('NO')
    
