T = input()

alphabet_list = ['','','','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
added_number = 0

for i in T:
    for j in alphabet_list:
        if i in j:
            added_number += alphabet_list.index(j)
            break

print(added_number)
