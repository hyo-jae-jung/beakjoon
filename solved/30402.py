from sys import stdin 

pixel = []
for _ in range(15):
    pixel.extend(stdin.readline().strip().split())

tmp = set(pixel)

if 'w' in tmp:
    print('chunbae')
elif 'b' in tmp:
    print('nabi')
elif 'g' in tmp:
    print('yeongcheol')
