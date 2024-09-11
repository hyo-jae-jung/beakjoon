from sys import stdin  

ans = []
while (i:=stdin.readline().strip()) != '0 0':
    numerator,denominator = map(int,i.split())
    ans.append(f"{numerator//denominator} {numerator%denominator} / {denominator}")

print(*ans,sep='\n')
