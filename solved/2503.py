from sys import stdin 

N = int(stdin.readline().strip())

questions = []
for _ in range(N):
    questions.append(tuple(stdin.readline().strip().split()))

ans = 0

def solution(num1,num2):
    s,b = 0,0
    for i in range(3):
        for j in range(3):
            if num1[i] == num2[j]:
                if i == j:
                    s+=1
                else:
                    b+=1
                break
    return s,b

for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if i == j or j == k or i == k:
                continue
            for num,s,b in questions:
                s2,b2 = solution(str(i)+str(j)+str(k),num)
                if int(s) != s2 or int(b) != b2:
                    break
            else:
                ans+=1

print(ans)
