from sys import stdin  

ans = []
while (a:=stdin.readline().strip()) != '#':
    alphabet = a[0]
    sentence = a[1:].strip()
    ans.append(alphabet + ' ' + str(sentence.lower().count(alphabet)))

print(*ans,sep='\n')
