from sys import stdin

T = int(stdin.readline().strip())

inp = []

for _ in range(T):
    inp.append(stdin.readline().strip())

def recursion(s, l, r, n):
    if l >= r: return 1, n
    elif s[l] != s[r]: return 0, n
    else: return recursion(s, l+1, r-1, n+1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 1)

for i in inp:
    print(*isPalindrome(i))
