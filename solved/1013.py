from sys import stdin 
import re

p1 = re.compile('100+1+')
p2 = re.compile('01')

T = int(stdin.readline().strip())

def is_pattern(s):
    while s:
        if (temp1:=p1.match(s)) or (temp2:=p2.match(s)):
            if temp1:
                e = temp1.end()
                cnt1 = s[:e].count('1')
                if e == len(s) or s[e:e+2] == '01':
                    s = s[e:]
                elif cnt1 > 2:
                    s = s[e-1:]
                else:
                    s = s[e:]
            else:
                s = s[temp2.end():]
        else:
            return 'NO'
    else:
        return 'YES'

answer = []
for _ in range(T):
    answer.append(is_pattern(stdin.readline().strip()))

print(*answer,sep='\n')
