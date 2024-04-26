from sys import stdin 

n = int(stdin.readline().strip())
ans = []
while (num:=int(stdin.readline().strip()))!=0:
    if num%n == 0:
        ans.append(f"{num} is a multiple of {n}.")
    else:
        ans.append(f"{num} is NOT a multiple of {n}.")

print(*ans,sep='\n')

