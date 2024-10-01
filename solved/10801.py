from sys import stdin   

A_nums = list(map(int,stdin.readline().strip().split()))
B_nums = list(map(int,stdin.readline().strip().split()))

A_scores,B_scores = 0,0

for i,j in zip(A_nums,B_nums):
    if i>j:
        A_scores+=1
    elif i<j:
        B_scores+=1
    
if A_scores>B_scores:
    print('A')
elif A_scores<B_scores:
    print('B')
else:
    print('D')
    