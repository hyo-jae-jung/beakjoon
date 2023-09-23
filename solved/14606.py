from sys import stdin 

N = int(stdin.readline().strip())
answer = 0
def pizza(n):
    if n==1:
        return True
    global answer
    a = n//2
    b = n-a
    answer+=a*b
    pizza(a)
    pizza(b)
    
pizza(N)

print(answer)
