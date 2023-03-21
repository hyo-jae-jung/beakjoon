from sys import stdin 

small,large = sorted(map(int,stdin.readline().strip().split()))

answer = 0

def sigma(n):
    n = abs(n)
    return n*(n+1)//2

if small > 0 and large > 0:
    answer = sigma(large) - sigma(small-1)
elif small < 0 and large > 0:
    answer = sigma(large) - sigma(small)
elif small == 0 and large > 0:
    answer = sigma(large) - sigma(small)
elif small == 0 and large == 0:
    answer = sigma(large) - sigma(small)
elif small < 0 and large == 0:
    answer = sigma(large) - sigma(small)
elif small < 0 and large < 0:
    answer = sigma(large+1) - sigma(small)

print(answer)
