from sys import stdin  

def conversion_number_system(n):
    i=0
    while n >= 26**(i+1):
        i+=1
    arr = [0]*(i+1)
    while i >= 0:
        if (t:=n//(26**i)) > 0:
            arr[i] = t
        n = n%(26**i)
        i-=1
    return arr

def conversion_digit(arr):
    for i in range(len(arr)-1):
        if arr[i] <= 0:
            arr[i]+=26
            arr[i+1]-=1
    if arr[-1] == 0:
        arr.pop()
    return arr

ans = []
while (S:=stdin.readline().strip()) != 'R0C0':
    A,c = S.split('C')
    r = A[1:]
    arr = conversion_number_system(int(c))
    arr = conversion_digit(arr)
    s = ''
    for i in map(lambda x:chr(x+64),arr):
        s = i + s
    s+=r
    ans.append(s)

print(*ans,sep='\n')
