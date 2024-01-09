from sys import stdin

now_hour,now_minute,now_second = map(int,stdin.readline().strip().split(':'))
start_hour,start_minute,start_second = map(int,stdin.readline().strip().split(':'))

def to_second(h,m,s):
    return h*60*60+m*60+s

now = to_second(now_hour,now_minute,now_second)
start = to_second(start_hour,start_minute,start_second)

diff = now - start

if diff < 0:
    diff*=-1
else:
    diff = 86400 - diff

diff_hour = diff//3600
diff_minute = (diff-diff_hour*3600)//60
diff_second = diff-diff_hour*3600-diff_minute*60

print(f"{str(diff_hour).zfill(2)}:{str(diff_minute).zfill(2)}:{str(diff_second).zfill(2)}")
