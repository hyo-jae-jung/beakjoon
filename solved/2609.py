import sys

A,B = map(int,sys.stdin.readline().strip().split())

def aliquot(N):
    n = []
    dev = 2
    while N != 1:
        if N%dev == 0:
            n.append(dev)
            N/=dev
        else:
            dev+=1
    return n

def exponent_cnt(list):
    dic = dict()
    for i in list:
        try:
            dic[i]+=1
        except:
            dic[i] = 1
    return dic

A_qliquot = exponent_cnt(aliquot(A))
B_qliquot = exponent_cnt(aliquot(B))
A_set = set(A_qliquot)
B_set = set(B_qliquot)

intersection = A_set & B_set

answer_a = 1

for i in intersection:
    answer_a*=i**min(A_qliquot[i],B_qliquot[i])

print(answer_a)

print(int(A/answer_a*B))
