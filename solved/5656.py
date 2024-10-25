from sys import stdin  

ans = []
while 'E' not in (s := stdin.readline().strip()):
    ans.append(eval(s))

for i,j in enumerate(ans,1):
    print(f"Case {i}: {str(j).lower()}")
