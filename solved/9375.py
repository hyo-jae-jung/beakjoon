from sys import stdin 
from collections import defaultdict 

T = int(stdin.readline().strip())
answer = []

def multiply(arr):
    answer = 1
    for i in arr:
        answer*=i+1
    return answer

for _ in range(T):
    
    int_dict = defaultdict(int)
    n = int(stdin.readline().strip())

    for _ in range(n):
        _,cat = stdin.readline().strip().split()
        int_dict[cat]+=1

    answer.append(multiply(list(int_dict.values()))-1)

print(*answer,sep='\n')
