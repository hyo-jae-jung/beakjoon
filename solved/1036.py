from sys import stdin 

### 입력 ###
N = int(stdin.readline().strip())
nums = []
for _ in range(N):
    nums.append(stdin.readline().strip())
K = int(stdin.readline().strip())
############

### 36진수 사전 ###
k = [str(i) for i in range(10)] + [chr(i+65) for i in range(26)]
it = [i for i in range(36)]
d = dict()
for i,j in zip(k,it):
    d[i],d[j]=j,i
###################


### Z 변경 ###
set_alphabet = set(sum([list(i) for i in nums],[]))
new_nums = []

if len(set_alphabet) > K:

    score_d = dict.fromkeys(set_alphabet,0)

    for i in nums:
        for j,k in enumerate(reversed(i)):
            score_d[k] += (int(d['Z'])-int(d[k]))*36**j

    score_t = []
    for i,j in score_d.items():
        score_t.append((i,j))

    score_t.sort(key=lambda x:x[1],reverse=True)

    change_nums = [score_t[i][0] for i in range(K)]

    for i in nums:
        temp = ''
        for j in i:
            if j in change_nums:
                temp+='Z'
            else:
                temp+=j
        else:
            new_nums.append(temp)
else:
    for i in nums:
        temp = ''
        for j in i:
            temp+='Z'*len(j)
        else:
            new_nums.append(temp)
#################################

def carculator_36(a:str,b:str)->str:

    def from_36_to_10(x:str)->int:
        answer = 0
        for i,j in enumerate(reversed(x)):
            answer+=int(d[j])*36**i
        return answer
    
    def from_10_to_36(x:int)->str:
        temp = []
        answer = ''
        while x//36 > 0:
            temp.append(x%36)
            x = x//36
        else:
            temp.append(x)
        while temp:
            answer+=d[temp.pop()]
        return answer
    
    return from_10_to_36(from_36_to_10(a)+from_36_to_10(b))

a = new_nums.pop()
while new_nums:
    b = new_nums.pop()
    a = carculator_36(a,b)

print(a)
