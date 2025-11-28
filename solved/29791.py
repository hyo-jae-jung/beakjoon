from sys import stdin  

N,M = map(int,stdin.readline().strip().split())
A = sorted(list(map(int,stdin.readline().strip().split())))
B = sorted(list(map(int,stdin.readline().strip().split())))

errd_nova = 100
origin_skill = 360

def solution(skill,arr):
    skill_cool,immun_cool,skill_cnt = 0,0,0
    before = 0
    for i in arr:
        skill_cool-=i-before
        immun_cool-=i-before
        if skill_cool <= 0 and immun_cool <= 0:
            skill_cnt+=1
            skill_cool = skill
            immun_cool = 90
        before = i
    return skill_cnt

print(solution(errd_nova,A),solution(origin_skill,B))
