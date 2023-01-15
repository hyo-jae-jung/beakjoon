from sys import stdin 
from collections import deque


inp = list(stdin.readline().strip())

cnt = 0
switch = deque(['0','1'])
criteria = inp.pop()

if criteria != switch[0]:
    switch.rotate()

while inp:
    temp = inp.pop()
    if temp != switch[0]:
        if switch[0] == criteria:
            cnt+=1
        switch.rotate()

print(cnt)
