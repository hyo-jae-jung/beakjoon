A, B = input().split()
C = input()

hour = int(A)
minute = int(B)
cooking_time = int(C)

new_minute = (minute + cooking_time)%60
new_hour = ((minute + cooking_time)//60 + hour)%24

print("{} {}".format(new_hour,new_minute))
