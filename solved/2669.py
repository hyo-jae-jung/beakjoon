from sys import stdin 

area = set()

def check_area(*args):
    tmp_set = set()
    for x in range(args[0],args[2]):
        for y in range(args[1],args[3]):
            tmp_set.add(y*100+x)
    return tmp_set

for _ in range(4):
    area|=check_area(*map(int,stdin.readline().strip().split()))

print(len(area))
