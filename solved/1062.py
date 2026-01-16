from sys import stdin  

N,K = map(int,stdin.readline().strip().split())
words = []
for _ in range(N):
    val = 0
    for i in set(stdin.readline().strip()[4:-4]):
        val+=2**(ord(i)-97)
    words.append(val)

default = list(map(lambda x:ord(x)-97,set("antatica")))
default_len = len(default)

if K < default_len:
    print(0)
else:
    letters = []
    visited = [False]*(26-default_len)

    default_val = 0
    for i in default:
        default_val+=2**i

    for i in range(26):
        if i not in default:
            letters.append(i)

    ans = 0
    def solution(val=default_val,cnt=K-default_len,idx=0):
        global words, letters, ans
        if cnt <= 0:
            tmp = 0
            for word in words:
                if (val & word) == word:
                    tmp+=1
            ans = max(ans,tmp)
            return 

        for i in range(idx,len(letters)):
            if not visited[i]:
                solution(val+2**letters[i],cnt-1,i+1)

    solution()
    print(ans)
