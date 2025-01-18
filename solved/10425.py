from sys import stdin  

T = int(stdin.readline().strip())

d = {0:0,1:1,2:1}
reverse = {0:0,1:2}
i = 3

def fibonacci(n):
    if d.get(n):
        return d[n]
    d.update({n:fibonacci(n-1)+fibonacci(n-2)})
    reverse.update({fibonacci(n-1)+fibonacci(n-2):n})
    return d[n]

def fibonacci_reverse(f):
    if reverse.get(f):
        return reverse[f]
    global i
    while not bool(reverse.get(f)):
        fibonacci(i)
        i+=1
    
    return reverse[f]

ans = []
for _ in range(T):
    F = int(stdin.readline().strip())
    ans.append(fibonacci_reverse(F))

print(*ans,sep='\n')
