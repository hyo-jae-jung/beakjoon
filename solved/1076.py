from sys import stdin 
d = dict()
d["black"] = '0'
d["brown"] = '1'
d["red"] = '2'
d["orange"] = '3'
d["yellow"] = '4'
d["green"] = '5'
d["blue"] = '6'
d["violet"] = '7'
d["grey"] = '8'
d["white"] = '9'

print(int(d[stdin.readline().strip()]+d[stdin.readline().strip()])*(10**int(d[stdin.readline().strip()])))
