from sys import stdin  

S = stdin.readline().strip()
print('YES' if (set(S) & set('MOBIS')) == set('MOBIS') else 'NO')
