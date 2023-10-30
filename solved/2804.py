from sys import stdin 
A,B = stdin.readline().strip().split()

overlap_words = set(A) & set(B)

for a in A:
    if a in overlap_words:
        first_overlap_word = a
        break

col_loc = A.index(first_overlap_word)
row_loc = B.index(first_overlap_word)

len_A = len(A)

for i,j in enumerate(B):
    if i == row_loc:
        print(A)
    else:
        tmp = ["."]*len_A
        tmp[col_loc] = j
        print(''.join(tmp))
