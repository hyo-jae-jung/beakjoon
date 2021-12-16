import sys
from math import pi


R = int(sys.stdin.readline().strip())

euclidean = pi*R**2
taxicab = 2*R**2

print(f"{euclidean:.6f}")
print(f"{taxicab:.6f}")