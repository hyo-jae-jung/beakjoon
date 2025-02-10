from sys import stdin   

ans = []

vowel = set(['a', 'e', 'i', 'o', 'u'])
while (s:=stdin.readline().strip()) != '#':
    
    i = 0
    while i < len(s):
        if s[i] in vowel:
            t = s[i:] + s[:i] + 'ay'
            break
        i+=1
    else:
        t = s + 'ay'

    ans.append(t)

print(*ans,sep='\n')

