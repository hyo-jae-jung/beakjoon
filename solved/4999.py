from sys import stdin 

jae = stdin.readline().strip()
doctor = stdin.readline().strip()

if len(jae) >= len(doctor):
    print('go')
else:
    print('no')
    