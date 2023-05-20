from sys import stdin 

N = int(stdin.readline().strip())

words = []
for _ in range(N):
    words.append(stdin.readline().strip())

selected = []

def check_word(s):
    s1 = s.split()
    answer = []
    
    for i in range(len(s1)):
        if s1[i][0].lower() not in selected:
            selected.append(s1[i][0].lower())
            return ' '.join(answer+['['+s1[i][0]+']'+s1[i][1:]]+s1[i+1:])
        else:
            answer.append(s1[i])
    
    answer = ''
    for i in range(len(s)):
        if s[i] != ' ':
            if s[i].lower() not in selected:
                answer+='['+s[i]+']'+s[i+1:]
                selected.append(s[i].lower())
                return answer
        answer+=s[i]

    return s

for i in words:
    print(check_word((i)))
