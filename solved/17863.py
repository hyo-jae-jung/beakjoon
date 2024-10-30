from sys import stdin  

num = stdin.readline().strip()
print('YES' if num[:3] == '555' else 'NO')
