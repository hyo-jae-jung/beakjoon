from sys import stdin  

ans = []
alphabets = ''
for i in range(65,65+26+1):
    alphabets+=chr(i)
while (s := stdin.readline().strip()) != '#':
    tmp = 0
    for i,j in enumerate(s,1):
        if j in alphabets:
            tmp+=i*(ord(j)-64)
    ans.append(tmp)

print(*ans,sep='\n')
