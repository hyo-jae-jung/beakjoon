from sys import stdin 
from bisect import bisect_left,bisect_right

arr = [1,2]
answer = []    
while (section:=stdin.readline().strip())!= '0 0':
    a,b = map(int,section.split())

    while arr[-1] <= b:
        i = len(arr)
        arr.append(arr[i-1]+arr[i-2])
    
    answer.append(bisect_right(arr,b) - bisect_left(arr,a))

print(*answer,sep='\n')
