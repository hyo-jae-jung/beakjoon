from sys import stdin 

ans = 0
vowels = set(['a','e','i','o','u'])
for a in stdin.readline().strip():
    if a in vowels:
        ans+=1
        
print(ans)
