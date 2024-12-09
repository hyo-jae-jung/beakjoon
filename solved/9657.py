from sys import stdin  

N = int(stdin.readline().strip())

arr = [
"SK",
"CY",
"SK",
"SK",
"SK",
"SK",
"CY",
]

print(arr[(N%7-1) if N%7 > 0 else 6])
