from sys import stdin  

antenna = int(stdin.readline().strip())
eyes = int(stdin.readline().strip())
ans = []

if antenna >= 3 and eyes <= 4:
    ans.append("TroyMartian")
if antenna <= 6 and eyes >= 2:
    ans.append("VladSaturnian")
if antenna <= 2 and eyes <= 3:
    ans.append("GraemeMercurian")

for i in ans:
    print(i)
