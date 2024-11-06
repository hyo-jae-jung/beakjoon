from sys import stdin  

ans = []
while (n:=int(stdin.readline().strip())) != 0:
    tmp = []
    for i in range(1,n+1):
        tmp.append("*"*i)
    ans.append(tmp)

for i in ans:
    for j in i:
        print(j)
        