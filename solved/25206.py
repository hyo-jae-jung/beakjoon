from collections import defaultdict 
grade = defaultdict(int)
grade['A+'] = 4.5
grade['A0'] = 4.0
grade['B+']	= 3.5
grade['B0']	= 3.0
grade['C+']	= 2.5
grade['C0']	= 2.0
grade['D+']	= 1.5
grade['D0']	= 1.0
grade['F']	= 0.0

score_x_grade = 0
scores = 0
for _ in range(20):
    _,score,rating = input().split()
    if rating != 'P':
        score_x_grade+=int(float(score))*grade[rating]
        scores+=int(float(score))
    
print(score_x_grade/scores)
