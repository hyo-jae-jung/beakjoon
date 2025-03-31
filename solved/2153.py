from sys import stdin  

S = stdin.readline().strip()
number = 0
for i in S:
    if (t:=ord(i)) > 96:
        number+=t-96
    else:
        number+=t-64+26

for i in range(2,int(number**0.5)+1):
    if number%i == 0:
        print("It is not a prime word.")
        break
else:
    print("It is a prime word.")

