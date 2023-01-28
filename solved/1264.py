from sys import stdin 
from bisect import bisect_left, bisect_right 

sentences = []
while True:
    temp = stdin.readline().strip()
    if temp == '#':
        break
    else:
        sentences.append(temp)

def binary_search(l:list,a:str)->int:
    return bisect_right(l,a)-bisect_left(l,a)

vowel = ['a', 'e', 'i', 'o', 'u']

for j in [sorted(i.lower()) for i in sentences]:
    cnt=0
    for k in vowel:
        cnt+=binary_search(j,k)
    print(cnt)
