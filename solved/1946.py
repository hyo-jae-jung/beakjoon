from sys import stdin

T = int(stdin.readline().strip())
answer = []
for _ in range(T):
    applicant_num = int(stdin.readline().strip())
    applicants = []
    for _ in range(applicant_num):
        applicants.append(tuple(map(int,stdin.readline().strip().split())))
    
    applicants.sort(key=lambda x:x[0])

    i,j = 0,1
    cnt = 1
    
    while j < len(applicants):
        if applicants[i][0] > applicants[j][0] or applicants[i][1] > applicants[j][1]:
            i=j
            cnt+=1
        j+=1
    else:
        answer.append(cnt)

print(*answer,sep='\n')
