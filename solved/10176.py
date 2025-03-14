from sys import stdin   

n = int(stdin.readline().strip())
ans = []
words = []
for _ in range(n):
    words.append([i for i in list(stdin.readline().strip().lower()) if 97<= ord(i) <= 97+26])
    
for i in range(n):
    while words[i]:
        a = words[i].pop()
        if (b:=chr(27-(ord(a)-96)+96)) in words[i]:
            words[i].remove(b)
        else:
            ans.append('No')
            break
    else:
        ans.append('Yes')

print(*ans,sep='\n')
