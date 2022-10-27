X = int(input())
N = int(input())
print( 'Yes 'if X == sum([eval('*'.join(list(map(str,input().split())))) for _ in range(N)]) else 'No')
