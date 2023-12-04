from sys import stdin 

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    loc,word = stdin.readline().strip().split()
    tmp=''
    loc = int(loc)
    for i in range(len(word)):
        if i != loc-1:
            tmp+=word[i]
    ans.append(tmp)

print(*ans,sep='\n')
