from sys import stdin  

A,B = stdin.readline().strip().split()
max_len = max(len(A),len(B))
print(''.join([str(int(i)+int(j)) for i,j in zip(list(A.zfill(max_len)),list(B.zfill(max_len)))]))
