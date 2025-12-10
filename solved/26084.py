from sys import stdin   
from math import comb

name_alphabet_cnt = [0]*26
for s in stdin.readline().strip():
    name_alphabet_cnt[ord(s)- 65]+=1

N = int(stdin.readline().strip())

alphabet_cnt = [0]*26
for _ in range(N):
    alphabet_cnt[ord(stdin.readline().strip()[0]) - 65]+=1

ans = 1
for i in range(26):
    if alphabet_cnt[i] < name_alphabet_cnt[i]:
        ans = 0
        break
    ans*=comb(alphabet_cnt[i],name_alphabet_cnt[i])

print(ans)
