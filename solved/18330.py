from sys import stdin   

n = int(stdin.readline().strip())
k = int(stdin.readline().strip())

print(n*1500 + ((n-k-60) if n>k+60 else 0)*1500)
