from sys import stdin 

N = int(stdin.readline().strip())
student_score = []
for _ in range(N):
    name,leng,eng,math = stdin.readline().strip().split()
    student_score.append((name,int(leng),int(eng),int(math)))

student_score.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))

for name,_,_,_ in student_score:
    print(name)
