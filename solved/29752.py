from sys import stdin  

_ = stdin.readline().strip()
print(max([len(i) for i in ''.join(['1' if int(i) > 0 else '0' for i in list(stdin.readline().strip().split())]).split('0')]))
