from sys import stdin  

d = {}
fighter_type = []

while (S:=stdin.readline().strip()) != '0':
    if S not in fighter_type:
        fighter_type.append(S)
        d.update({S:0})
    d[S]+=1

grand_total = 0
for fighter in fighter_type:
    print(f"{fighter}: {d[fighter]}")
    grand_total+=d[fighter]
print(f"Grand Total: {grand_total}")
