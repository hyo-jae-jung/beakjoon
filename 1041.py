from sys import stdin 

N = int(stdin.readline().strip())
dice = dict()
for k,j in enumerate([int(i) for i in stdin.readline().strip().split()]):
    dice[chr(k+65)]=j

