from sys import stdin 

S = stdin.readline()
def check(s):
    for i in [i for i in s.split('pi') if i]:
        for j in [j for j in i.split('ka') if j]:
            print(j)
            if j not in ['','chu']:
                return 'NO'
                
    return 'YES'

print(check(S))
