from sys import stdin 

N = int(stdin.readline().strip())
M = int(stdin.readline().strip())
seq_nums = []
seat = 0
for _ in range(M):
    vip_seat = int(stdin.readline().strip())
    seat_len = vip_seat-seat-1
    if seat_len > 0:
        seq_nums.append(seat_len)
    seat = vip_seat

if (last_seat_len:=N - seat) > 0:
    seq_nums.append(last_seat_len)

ans = 1
if seq_nums:
    max_seq_nums = max(seq_nums)

    dp = [[0]*(max_seq_nums+1) for _ in range(2)]
    dp[0][1] = 1
    for i in range(1,max_seq_nums):
        dp[0][i+1] = dp[0][i]+dp[1][i]
        dp[1][i+1] = dp[0][i]

    for num in seq_nums:
        ans*=(dp[0][num]+dp[1][num])

print(ans)
