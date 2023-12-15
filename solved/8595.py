from sys import stdin 
import re

_ = stdin.readline().strip()
print(sum(int(i) for i in re.sub('\D',',',stdin.readline().strip()).split(',') if i))
