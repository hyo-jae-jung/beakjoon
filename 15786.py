from sys import stdin  
import re 

N,M = map(int,stdin.readline().strip().split())
pattern = ".*"+".*".join(stdin.readline().strip())+".*"
ans = []
for _ in range(M):
    ans.append(str(bool(re.search(pattern,stdin.readline().strip()))).lower())

print(*ans,sep='\n')
