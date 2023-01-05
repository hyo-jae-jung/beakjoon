from sys import stdin

fomula = stdin.readline().strip()

num = []
pm = []
temp=''
for i in fomula:
    if i not in ['+','-']:
        temp+=i
    else:
        num.append(int(temp))
        pm.append(i)
        temp = ''
else:
    num.append(int(temp))

if '-' in pm:
    i = pm.index('-')
    pm = ['+']*i + ['-']*(len(pm)-i)

answer = str(num[0])
for i,j in zip(num[1:],pm):
    answer+=str(j)+str(i)

print(eval(answer))
