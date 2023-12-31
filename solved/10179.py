from sys import stdin 

ans = []
for _ in range(int(stdin.readline().strip())):
    ans.append("${:.2f}".format(float(stdin.readline().strip())*0.8))

print(*ans,sep='\n')
