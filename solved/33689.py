from sys import stdin  

N = int(stdin.readline().strip())
S = [1 if stdin.readline().strip()[0] == 'C' else 0 for _ in range(N)]
print(sum(S))
