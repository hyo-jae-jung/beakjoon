from sys import stdin 

N = int(stdin.readline().strip())
P = [int(i) for i in stdin.readline().strip().split()]
S = [int(i) for i in stdin.readline().strip().split()]

def find_cnt(n,p,s):

    players = [0,1,2]*(n//3)

    def mix(pl:list, seq:list)->list:
        answer = []
        for i in seq:
            answer.append(pl[i])
        return answer




print(find_cnt(N,P,S))
