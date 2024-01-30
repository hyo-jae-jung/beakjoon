from sys import stdin 
import re 

S = stdin.readline().strip()
P = stdin.readline().strip()

p = re.compile(P)
print(1 if bool(p.search(S)) else 0)
