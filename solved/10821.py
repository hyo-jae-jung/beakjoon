from sys import stdin 

S = stdin.readline().strip().split(',')
ans = 0
for i in S:
    try:
        int(i)
        ans+=1
    except:
        pass

print(ans)
