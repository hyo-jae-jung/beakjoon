from sys import stdin 

k = stdin.readline().strip()

def solution(k):
    if len(k) > 2:
        diff = int(k[1]) - int(k[0])
        for i in range(2,len(k)):
            if int(k[i]) - int(k[i-1]) != diff:
                return "흥칫뿡!! <(￣ ﹌ ￣)>"
                
    return "◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!"

print(solution(k))
