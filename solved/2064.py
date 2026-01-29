from sys import stdin  

n = int(stdin.readline().strip())
locs = []
for _ in range(n):
    locs.append(''.join(list(map(lambda x:bin(int(x))[2:].zfill(8),stdin.readline().strip().split('.')))))

m = 0
for i in range(n-1):
    for j in range(i+1,n):
        c,b = bin(~(int(locs[i],2) ^ int(locs[j],2)) + 1).split('b')
        if int(b) > 0:
            m = max(m,len(b))

network_mask = []
for i in range((32-m)//8):
    network_mask.append(255)

if len(network_mask) < 4:
    network_mask.append(int('1'*(e:=(32-m)%8)+'0'*(8-e),2))

while len(network_mask) < 4:
    network_mask.append(0)

min_network = locs[0][:32-m]+'0'*m

print('.'.join(list(map(lambda x:str(int(x,2)),[min_network[:8],min_network[8:16],min_network[16:24],min_network[24:32]]))))
print('.'.join(list(map(str,network_mask))))
