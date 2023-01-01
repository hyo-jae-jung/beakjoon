from sys import stdin

input = stdin.readline().strip()
output = bin(int(input,8))[2:]

print(output)
