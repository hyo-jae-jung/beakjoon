T = int(input())

RS = []
for i in range(T):
    RS.append(input().split())

answer = []
t = ""

for i in RS:
    for j in i[1]:
        for k in range(int(i[0])):
            t += j
    answer.append(t)
    t = ""

for i in answer:
    print(i)