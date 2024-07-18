from sys import stdin  

ans = []
while (xy:=stdin.readline().strip()) != "0 0":
    x,y = list(map(float,xy.split()))

    if x == 0 or y == 0:
        ans.append("AXIS")
    elif x > 0 and y > 0:
        ans.append("Q1")
    elif x < 0 and y > 0:
        ans.append("Q2")
    elif x < 0 and y < 0:
        ans.append("Q3")
    elif x > 0 and y < 0:
        ans.append("Q4")
else:
    ans.append("AXIS")

print(*ans,sep='\n')
