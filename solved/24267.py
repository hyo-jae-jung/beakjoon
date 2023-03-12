from sys import stdin 
n = int(stdin.readline().strip())
print(sum([i*j for i,j in zip(range(1,n-1,1),range(n-2,0,-1))]),3,sep='\n')
