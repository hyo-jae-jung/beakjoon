import sys
from collections import deque

def rot13(x:int)->int:
    default = 97 if x > 96 else 65
    return x+13 if x+13 < default+26 else x+13-26

sentence = sys.stdin.readline()[:-1]

answer = ''

for i in sentence:
    
    try:
        int(i)
        answer+=i
    except:
        if i != ' ':
            answer+=chr(rot13(ord(i)))
        else:
            answer+=i
        
print(answer)
