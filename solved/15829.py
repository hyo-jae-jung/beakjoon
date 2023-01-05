from sys import stdin

L = int(stdin.readline().strip())
alphabet = stdin.readline().strip()
r = 31
M = 1234567891

d = {}
for i in range(1,27):
    d[chr(96+i)]=i 

H = 0
for i in range(len(alphabet)):
    H+=d[alphabet[i]]*r**i
H%=M

print(f'{H}')
