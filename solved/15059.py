from sys import stdin  

ca,ba,pa = map(int,stdin.readline().strip().split())
cr,br,pr = map(int,stdin.readline().strip().split())
print((cr-ca if cr > ca else 0)+(br-ba if br > ba else 0)+(pr-pa if pr > pa else 0))
