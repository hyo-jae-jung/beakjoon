sang_gun_input = map(int,input().split())

def sang_su_understand(x:int):
    answer = ""
    for i in reversed(str(x)):
        answer += i
    return answer

sang_su_output = []

for i in sang_gun_input:
    sang_su_output.append(sang_su_understand(i))

print(max(sang_su_output))