from sys import stdin

ans = int(stdin.readline().strip())
while (s:=stdin.readline().strip()) !="=":
    ss = int(stdin.readline().strip())
    if s == '+':
        ans+=ss
    elif s == '-':
        ans-=ss
    elif s == '*':
        ans*=ss
    elif s == '/':
        ans = ans//ss

print(ans)
    