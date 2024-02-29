from sys import stdin 
import pdb
T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    alphabet_cnt = [0]*26
    M = stdin.readline().strip()
    i=0
    while i < len(M):
        alphabet_cnt[ord(M[i])-65]+=1
        if alphabet_cnt[ord(M[i])-65] == 3:
            if i == len(M)-1:
                if alphabet_cnt[ord(M[i])-65] == 3:
                    ans.append('FAKE')
                    break
            elif M[i+1] != M[i]:
                ans.append('FAKE')
                break
            else:
                alphabet_cnt[ord(M[i])-65] = 0
                i+=2
        i+=1
    else:
        ans.append('OK')

print(*ans,sep='\n')
