from sys import stdin  

S = stdin.readline().strip()
d = {}
suffix_arr = [(len(S)-1,S[-1])]
for i,j in zip(reversed(S[:-1]),range(len(S)-2,-1,-1)):
    suffix_arr.append((j,i+suffix_arr[-1][1]))
    
for i,_ in sorted(suffix_arr,key=lambda x:x[1]):
    print(i)
