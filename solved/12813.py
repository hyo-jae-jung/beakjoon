from sys import stdin  

A = stdin.readline().strip()
B = stdin.readline().strip()

print(bin(int('0b'+A,2) & int('0b'+B,2))[2:].zfill(100000))
print(bin(int('0b'+A,2) | int('0b'+B,2))[2:].zfill(100000))
print(bin(int('0b'+A,2) ^ int('0b'+B,2))[2:].zfill(100000))

def not_X(x):
    not_X = ''
    for i in x:
        if i == '0':
            not_X+='1'
        else:
            not_X+='0'
    print(not_X)

not_X(A)
not_X(B)
