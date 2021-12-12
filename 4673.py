def d(n:int):
  answer = n
  m = str(n)
  for i in m:
    answer += int(i)
  return answer

no_self_number_list =[]
self_number_list = []

for start_number in range(1,10001):
  if start_number not in no_self_number_list:
    self_number_list.append(start_number)
    number = start_number
    while number <= 10000:
        number = d(number)
        if number not in no_self_number_list:
            no_self_number_list.append(number)
        else:
            break

for i in self_number_list:
  print(i)