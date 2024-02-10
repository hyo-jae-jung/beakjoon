from sys import stdin 
ans = []
while (n:=int(stdin.readline().strip())) != 0:
    words = []
    for _ in range(n):
        words.append(stdin.readline().strip())

    words.sort(key=lambda x:x.lower())
    ans.append(words[0])

print(*ans,sep='\n')
