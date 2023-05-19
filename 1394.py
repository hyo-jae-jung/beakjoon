from sys import stdin 
from collections import defaultdict
from bisect import bisect_right

letters = stdin.readline().strip()
password = stdin.readline().strip()
# letters = sorted(list(letters))
answer = 0
l = len(letters)
d = defaultdict(int)
for i,j in enumerate(reversed(password)):
    if not d[j]:
        d[j] = bisect_right(letters,j)
    answer+=d[j]*l**i
        
print(answer%900528)
