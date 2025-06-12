from sys import stdin  

S = stdin.readline().strip()
N = int(stdin.readline().strip())
words = [stdin.readline().strip() for _ in range(N)]

ans = True
for i in range(26):
    if ans == True:
        tmp = ''
        for j in S:
            tmp+=chr((ord(j)-97+i)%26+97)
        
        for word in words:
            if word in tmp:
                ans = tmp    
                break

print(ans)
