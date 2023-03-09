N,M = map(int,input().split())
pack = []
ea = []
for _ in range(M):
    p,e = map(int,input().split())
    pack.append(p)
    ea.append(e)
    
pack_num = N//6
ea_num = N%6

print(pack_num*min(min(pack),min(ea)*6) + min(min(pack),ea_num*min(ea)))
