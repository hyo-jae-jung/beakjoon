from sys import stdin 

N,P,Q = [int(i) for i in stdin.readline().strip().split()]

arr = [1]

def seq(n:int,p:int,q:int)->int:
    if n < len(arr):
        return arr[n]
    else:
        num = seq(n//p,p,q)+seq(n//q,p,q)
        print(seq(n//p,p,q),seq(n//q,p,q))
        arr.append(num)
    return num

print(seq(N,P,Q),arr)
