from sys import stdin  

ans = []

while (n:=int(stdin.readline().strip())) != 0:
    arr = []
    i = 0
    for _ in range(n):
        arr.append(stdin.readline().strip())

    for j in arr:
        t = j[i:].find(' ') 
        i+= len(j[i:]) if t == -1 else t

    ans.append(i+1)

print(*ans,sep='\n')
