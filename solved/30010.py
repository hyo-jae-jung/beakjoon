from sys import stdin   

N = int(stdin.readline().strip())
print(*([N]+list(range(1,N))))
