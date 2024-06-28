from sys import stdin  

STR,DEX,INT,LUK,N = map(int,stdin.readline().strip().split())

tmp = N*4-(STR+DEX+INT+LUK)

print(tmp if tmp >=0 else 0)
