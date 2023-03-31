from sys import stdin 
from collections import defaultdict 
n = int(stdin.readline().strip())
log = defaultdict(bool)
for _ in range(n):
    name,state = stdin.readline().strip().split()
    if state == 'enter':
        log[name] = True
    elif state == 'leave':
        try:
            log.pop(name)
        except:
            pass
        
print(*sorted(log.keys(),reverse=True),sep='\n')
