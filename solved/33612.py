from sys import stdin   

N = int(stdin.readline().strip())

year,month = 2024,1

if (month+N*7)%12 == 0:
    print(year+(month+N*7)//12-1,12)
else:
    print(year+(month+N*7)//12,(month+N*7)%12)
