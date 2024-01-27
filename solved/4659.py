from sys import stdin 

vowels = {'a','e','i','o','u'}
except_vowel = {'e','o'}
ans = []
while (word:=stdin.readline().strip()) != 'end':
    is_a_vowel_in_this_word = False
    seq_count = 0
    before_alphabet = ''
    is_vowel = True

    before_vowel = 'first'
    for i in word:
        if i in vowels:
            is_vowel = True
        else:
            is_vowel = False

        if (not is_a_vowel_in_this_word) and is_vowel:
            is_a_vowel_in_this_word = True

        if before_vowel == is_vowel:
            seq_count+=1
            if ((i not in except_vowel) and (before_alphabet == i)) or seq_count > 2:
                is_a_vowel_in_this_word = False
                break
        else:
            seq_count = 1
        before_vowel = is_vowel
        before_alphabet = i
    
    if is_a_vowel_in_this_word:
        ans.append(f"<{word}> is acceptable.")
    else:
        ans.append(f"<{word}> is not acceptable.")

print(*ans,sep='\n')
