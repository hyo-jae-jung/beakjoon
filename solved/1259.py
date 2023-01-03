from sys import stdin
import math

num_list = []
while True:
    temp = stdin.readline().strip()
    if not int(temp):
        break
    num_list.append(temp)

for i in num_list:
    l = len(i)
    if i[:int(l/2)] == ''.join(reversed(i[math.ceil(l/2):])):
        print('yes')
    else:
        print('no')
