from sys import stdin   

adjacency_list = [[] for _ in range(9)]
adjacency_list[1].extend([4,5])
adjacency_list[3].extend([4,5])
adjacency_list[4].extend([2,3])
adjacency_list[5].extend([8])
adjacency_list[6].extend([2,3])
adjacency_list[7].extend([8])
adjacency_list[8].extend([6,7])

ans = []

idx = 0
while (S:=stdin.readline().strip()) != '0':
    idx+=1
    if S[0] != '1' or S[-1] != '2':
        ans.append(f"{idx}. NOT")
        continue

    for i in range(1,len(S)):
        if int(S[i]) not in adjacency_list[int(S[i-1])]:
            ans.append(f"{idx}. NOT")
            break
    else:
        ans.append(f"{idx}. VALID")
if ans:
    print(*ans,sep='\n')
