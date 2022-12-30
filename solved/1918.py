
import sys

N = int(sys.stdin.readline().strip())
formula = list(sys.stdin.readline().strip())
d = {}
for i,_ in enumerate(range(N)):
    d[chr(65+i)] = int(sys.stdin.readline().strip())

for i in range(len(formula)):
    if formula[i] not in ['+','-','*','/']:
        formula[i] = d[formula[i]]

i=0
while len(formula) > 1:
    if formula[i] in ['+','-','*','/']:
        temp = str(formula[i-2])+str(formula[i])+str(formula[i-1])
        formula = formula[:i-2] + [eval(temp)] + formula[i+1:]
        i=0
    else:
        i+=1

print('{:.2f}'.format(*formula))
