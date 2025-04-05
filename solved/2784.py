from sys import stdin  
from itertools import permutations as perm

def solution(word,words):
    copy_words = words.copy()
    for j in range(3):
        a = ''
        for k in range(3*j,3*(j+1)):
            a+=word[k]
        t = ''
        for i in range(j,9,3):
            t+=word[i]
        if a in copy_words:
            copy_words.remove(a)
        else:
            return False
        
        if t in copy_words:
            copy_words.remove(t)
        else:
            return False
    else:
        if not copy_words:
            return True
        else:
            return False
        
words = []
for _ in range(6):
    words.append(stdin.readline().strip())

ans = []
for i in perm(words,3):
    l = ''.join(i)
    if solution(l,words):
        ans.append(l)
if ans:
    result = sorted(ans)[0]
    for i in range(0,9,3):
        tep = ''
        for j in range(i,i+3):
            tep+=result[j]
        print(tep)
else:
    print(0)
