from sys import stdin  

S,E,Q = stdin.readline().strip().split()
items = stdin.read().strip()
lines = items.splitlines()
p_users = set()

def mm(time):
    hh,mm = map(int,time.split(":"))
    return hh*60+mm

s_val = mm(S)
e_val = mm(E)
q_val = mm(Q)

ans = 0
for line in lines:
    time,user = line.split()
    val = mm(time)
    if (user not in p_users) and (val <= s_val):
        p_users.add(user)
    if (user in p_users) and (e_val <= val <= q_val):
        ans+=1
        p_users.discard(user)

print(ans)
