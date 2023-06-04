from sys import stdin

N = int(stdin.readline().strip())
num_set = set()

k = 1
while (tetrahedron:=(k*(k+1)*(2*k+1)//6+k*(k+1)//2)//2) <= N:
    num_set.add(tetrahedron)
    k+=1
    
num_list = sorted(list(num_set),reverse=True)
