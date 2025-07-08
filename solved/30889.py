from sys import stdin  

N = int(stdin.readline().strip())
seats = [['.']*20 for _ in range(10)]
for _ in range(N):
    seat_num = stdin.readline().strip()
    seats[ord(seat_num[0]) - 65][int(seat_num[1:])-1] = 'o'

for i in seats:
    print(''.join(i))
