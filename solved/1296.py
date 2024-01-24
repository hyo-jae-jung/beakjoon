from sys import stdin 

e_name = stdin.readline().strip()
N = int(stdin.readline().strip())
team_name_rate = []
for _ in range(N):
    team_name = stdin.readline().strip()
    d = {
        'L':0,'O':0,'V':0,'E':0
    }
    for i in e_name+team_name:
        try:
            d[i]+=1
        except:
            pass
    
    team_name_rate.append(((d['L']+d['O'])*(d['L']+d['V'])*(d['L']+d['E'])*(d['O']+d['V'])*(d['O']+d['E'])*(d['V']+d['E'])%100,team_name))

team_name_rate.sort(key=lambda x:(-x[0],x[1]))

print(team_name_rate[0][1])
