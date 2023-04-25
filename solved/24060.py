from sys import stdin 

A,K = map(int,stdin.readline().strip().split())
A = [int(i) for i in stdin.readline().strip().split()]
answer = [0]

def merge(L,left,mid,right):
    i,j = left,mid+1
    temp = []
    while i <= mid and j <= right:
        if L[i] < L[j]:
            temp.append(L[i])
            i+=1
        else:
            temp.append(L[j])
            j+=1
    
    while i <= mid:
        temp.append(L[i])
        i+=1

    while j <= right:
        temp.append(L[j])
        j+=1
    for i,j in zip(range(left,right+1),temp):
        L[i] = j
        answer.append(j)

def division(L,left,right):
    if left < right:
        mid = (left+right)//2
        division(L,left,mid)
        division(L,mid+1,right)
        merge(L,left,mid,right)

division(A,0,len(A)-1)
try:
    print(answer[K])
except:
    print(-1)
