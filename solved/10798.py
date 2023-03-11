from sys import stdin 

samples = []
each_sample_len = []

while True:
    temp = list(stdin.readline().strip())
    if temp:
        samples.append(temp)
        each_sample_len.append(len(temp))
    else:
        break
    
max_sample_len = max(each_sample_len)

new_samples = []
for i in samples:
    new_samples.append(i+[' ']*(max_sample_len-len(i)))

arr_cnt = len(new_samples)
one_line = sum(new_samples,[])

print(''.join(sum([one_line[i::max_sample_len] for i in range(max_sample_len)],[])).replace(' ',''))
    