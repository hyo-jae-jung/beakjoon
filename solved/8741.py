from sys import stdin  

k = int(stdin.readline().strip())
i = int('1'*k,2)
print(bin(i*(i+1)//2)[2:])
