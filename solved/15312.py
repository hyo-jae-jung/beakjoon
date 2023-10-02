from sys import stdin 

A = list(stdin.readline().strip())
B = list(stdin.readline().strip())
d = dict()
for i,j in enumerate([3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]):
    d[chr(i+65)] = j

mixed_names=''
for i,j in zip(A,B):
    mixed_names+=i+j

change_from_name_to_num = []
for i in mixed_names:
    change_from_name_to_num.append(d[i])

def chemistry(s:str)->str:
    
    l = len(s)
    while l > 2:
        tmp = []
        for i in range(1,l):
            tmp.append(int(str(s[i]+s[i-1])[-1]))
        s = tmp
        l = len(s)
    return s

print(''.join(map(str,chemistry(change_from_name_to_num))))
