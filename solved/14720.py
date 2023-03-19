from sys import stdin 

N = int(stdin.readline().strip())
milk_stores = map(int,stdin.readline().strip().split())
liking = [0,1,2]
liking_len = len(liking)
answer_cnt = 0
for i in milk_stores:
    if i == liking[answer_cnt%liking_len]:
        answer_cnt+=1
        
print(answer_cnt)
