from sys import stdin 
from collections import defaultdict 

word1 = stdin.readline().strip()
word2 = stdin.readline().strip()

word1_cnt = defaultdict(int)
word2_cnt = defaultdict(int)

for i in word1:
    word1_cnt[i]+=1
 
for i in word2:
    word2_cnt[i]+=1
 
ans = len(word1)+len(word2)

for i in set(word1_cnt.keys()) & set(word2_cnt.keys()):
    ans-=min(word1_cnt[i],word2_cnt[i])*2

print(ans)
