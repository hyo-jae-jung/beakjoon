from sys import stdin 
from bisect import bisect_left, bisect_right

first_alphabet = []
first_alphabet_dict = {}

for _ in range(int(stdin.readline().strip())):
    first_alphabet.append(stdin.readline().strip()[0])

first_alphabet.sort()

fa_set = set(first_alphabet)

def binary_search(arr:list,x:str)->int:
    return bisect_right(arr,x) - bisect_left(arr,x)

for i in fa_set:
    first_alphabet_dict[i] = binary_search(first_alphabet,i)

answer = ''.join(sorted([i for i,j in first_alphabet_dict.items() if j>4]))

if answer:print(answer)
else:print('PREDAJA')
