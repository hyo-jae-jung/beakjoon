from sys import stdin 

B1 = stdin.readline().strip()
B2 = stdin.readline().strip()

print(bin(int(B1,2)*int(B2,2))[2:])
