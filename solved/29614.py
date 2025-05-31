from sys import stdin  

S = stdin.readline().strip()
table = {
    'A+':4.5,
    'A':4.0,
    'B+':3.5,
    'B':3.0,
    'C+':2.5,
    'C':2.0,
    'D+':1.5,
    'D':1.0,
    'F':0.0,
         }

val = 0
cnt = 0

s = ''
for i in S:
    if s == '':
        s=i
    elif i == '+':
        s+=i
    else:
        val+=table[s]
        cnt+=1
        s = i

val+=table[s]
cnt+=1

print(val/cnt)
