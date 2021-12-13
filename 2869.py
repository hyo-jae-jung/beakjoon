import math

A,B,V = map(int,input().split())

day = math.ceil((V-B)/(A-B))

print(day)


