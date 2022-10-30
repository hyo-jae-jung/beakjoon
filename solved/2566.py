table = []
for _ in range(9):
    table.append(list(map(int,input().split())))

max_num = max(sum(table,[]))

for i,l in enumerate(table,1):
    if max_num in l:
        print(max_num)
        print("{} {}".format(i,l.index(max_num)+1))
        break