from sys import stdin 
from collections import defaultdict 

N = int(stdin.readline().strip())
extensions_dict = defaultdict(int)
for _ in range(N):
    _,extension = stdin.readline().strip().split('.')
    extensions_dict[extension]+=1

extensions_list = []
for i,j in zip(extensions_dict.keys(),extensions_dict.values()):
    extensions_list.append((i,j))

extensions_list.sort(key=lambda x:x[0])

for i in extensions_list:
    print(*i)
