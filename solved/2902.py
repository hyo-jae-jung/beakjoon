from sys import stdin 

word = stdin.readline().strip().split('-')
ans = ''
for i in word:
    ans+=i[0].upper()

print(ans)
