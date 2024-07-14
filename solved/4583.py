from sys import stdin  

mirror_words_a = ['i','o','v','w','x']
mirror_words_b = ['b','d']
mirror_words_c = ['p','q']
ans = []
while (i:=stdin.readline().strip())!='#':
    if set(i) - set(mirror_words_a) - set(mirror_words_b) - set(mirror_words_c):
        ans.append('INVALID')
    else:
        t= ''
        for i in reversed(i):
            if i in mirror_words_b:
                t+=mirror_words_b[(mirror_words_b.index(i)+1)%2]
            elif i in mirror_words_c:
                t+=mirror_words_c[(mirror_words_c.index(i)+1)%2]
            else:
                t+=i
        ans.append(t)
        
print(*ans,sep='\n')
