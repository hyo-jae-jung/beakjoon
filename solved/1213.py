from sys import stdin 

NAME = stdin.readline().strip()

def solution(name:str)->str:

    name_length = len(name)
    alphabet_cnt = dict.fromkeys(set(name),0)
    for i in name:
        alphabet_cnt[i]+=1
    
    is_odd = [i%2 == 1 for i in alphabet_cnt.values()]

    def palindrome(name):
        answer = []
        center = ''
        if any(is_odd):
            center = list(alphabet_cnt.keys())[is_odd.index(True)]

        for i in sorted(list(set(name))):
            answer+=[i]*(alphabet_cnt[i]//2)

        return ''.join(answer + [center] + list(reversed(answer)))

    if sum(is_odd) > name_length%2:
        return 'I\'m Sorry Hansoo'
    else:
        return palindrome(name)
    
print(solution(NAME))
