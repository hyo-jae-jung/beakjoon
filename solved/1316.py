word_count = int(input())
words_list = []

for _ in range(word_count):
    words_list.append(input())

no_sequence_check_count = 0

for h in words_list:

    alphabet_list = []  

    for i in range(len(h)-1):
        if h[i] != h[i+1]:
            alphabet_list.append(h[i])
    alphabet_list.append(h[-1])

    alphabet_list.sort()
    
    for i in range(len(alphabet_list)-1):
        if alphabet_list[i] == alphabet_list[i+1]:
            no_sequence_check_count += 1
            break

print(word_count - no_sequence_check_count)