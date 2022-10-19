T = input()
input_text_length = len(T)

c_alphabet_list = ["c=","c-","dz=","d-","lj","nj","s=","z="]
c_alphabet_count = 0

while input_text_length > 0:
    
    if T[:2] in c_alphabet_list:
        T = T[2:]
        input_text_length -= 2
    elif T[:3] in c_alphabet_list:
        T = T[3:]
        input_text_length -= 3
    else:
        T = T[1:]
        input_text_length -= 1

    c_alphabet_count += 1

print(c_alphabet_count)