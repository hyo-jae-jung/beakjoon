from sys import stdin 

answer = []
s = set(range(1,11))
while n:=int(stdin.readline().strip()):
    if (sten:=stdin.readline().strip()) == "too high":
        for i in range(n,11):
            s.discard(i)
    elif sten == "too low":
        for i in range(1,n+1):
            s.discard(i)
    else:
        if n in s:
            answer.append("Stan may be honest")
        else:
            answer.append("Stan is dishonest")
        s = set(range(1,11))

print(*answer,sep='\n')
