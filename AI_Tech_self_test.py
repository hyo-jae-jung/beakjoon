T = input()

def is_palindrome(text:str):

    for i in range(round(len(text)/2)):
        if text[i] != text[-1-i]:
            return -1
            break
    return 1

a = is_palindrome(T)
print(a)