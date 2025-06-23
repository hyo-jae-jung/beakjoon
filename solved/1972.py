from sys import stdin  

ans = []

def solution(S):
    l = len(S)
    for i in range(1,l):
        s = set()
        for j in range(i,l):
            if S[j]+S[j-i] in s:
                return f"{S} is NOT surprising."
            s.add(S[j]+S[j-i])

    return f"{S} is surprising."

while (S:=stdin.readline().strip()) != "*":
    ans.append(solution(S))

print(*ans,sep='\n')
