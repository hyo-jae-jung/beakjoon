from sys import stdin 

N,M = map(int,stdin.readline().strip().split())

cnt = 0
def split_up_chocolate(n,m):
    global cnt
    if n == 1 and m == 1:
        return None
    if n >= m:
        cnt+=1
        split_up_chocolate(n//2,m)
        split_up_chocolate(n-n//2,m)
    elif n < m:
        cnt+=1
        split_up_chocolate(n,m//2)
        split_up_chocolate(n,m-m//2)
        
split_up_chocolate(N,M)
print(cnt)
