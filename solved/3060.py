from sys import stdin 

T = int(stdin.readline().strip())
answer = []
for _ in range(T):
    feed_total = int(stdin.readline().strip())
    pigs_feed = list(map(int,stdin.readline().strip().split()))
    cnt = 1

    while feed_total >= sum(pigs_feed):
        cnt+=1
        tmp_feed = [0]*6
        for i in range(6):
            tmp_feed[i] = pigs_feed[i] + pigs_feed[(i-1)%6] + pigs_feed[(i+1)%6] + pigs_feed[(i+3)%6]
        pigs_feed = tmp_feed

    answer.append(cnt)

print(*answer,sep='\n')
