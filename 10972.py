import sys
from itertools import permutations as perm
import pdb

N = int(sys.stdin.readline().strip())

perms = list(perm(range(1,N+1),N))
perm_idx = perms.index(tuple(map(int,sys.stdin.readline().strip().split())))

pdb.set_trace()

try:
    print(' '.join(map(str,perms[perm_idx+1])))
except:
    print(-1)
