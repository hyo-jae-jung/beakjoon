from sys import stdin 

ans = []
while (s := stdin.readline().strip()) != str(-1):
    tmp = 0
    m = [False]*201
    nums = list(map(int,s.split(' ')[:-1]))
    for i in nums:
        m[i] = True
    
    for i in nums:
        if m[i*2]:
            tmp+=1

    ans.append(tmp)

print(*ans,sep='\n')
