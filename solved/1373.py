import sys

input = sys.stdin.readline().strip()
output = oct(int(input,2))[2:]
print(output)
