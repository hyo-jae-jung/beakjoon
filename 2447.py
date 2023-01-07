from sys import stdin

def empty(n:int)->str:
    if n==1:
        return 'a'
    else:
        answer = ''
        for _ in range(3):
            for _ in range(3):
                answer+=empty(n-1)
            answer+='\n'
        return answer.strip()

def star(n:int)->str:
    if n==1:
        return '*'
    else:
        temp = ''
        for i in range(3):
            for i in range(3):
                temp+=star(n-1)
            temp+='\n'
        return temp
        
if __name__ == "__main__":
    print(empty(int(stdin.readline().strip())))
