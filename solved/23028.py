from sys import stdin 

N,A,B = map(int,stdin.readline().strip().split())
criteria_major = 66
criteria_culture = 130

subjects = []
for _ in range(10):
    subjects.append(tuple(map(int,stdin.readline().strip().split())))


for i in range(8-N):
    A+=subjects[i][0]*3
    B+=subjects[i][0]*3 + ((6-subjects[i][0]) if (6-subjects[i][0]) < subjects[i][1] else subjects[i][1])*3

if A >= criteria_major and B >= criteria_culture:
    print("Nice")
else:
    print("Nae ga wae")

