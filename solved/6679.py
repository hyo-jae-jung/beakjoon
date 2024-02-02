def convert_notation_and_sum(from_x,to_n):
    tmp = 0
    while from_x:
        tmp+=from_x%to_n
        from_x = from_x//to_n
    return tmp


for i in range(1000,10000):
   if convert_notation_and_sum(i,10) == convert_notation_and_sum(i,12) == convert_notation_and_sum(i,16):
        print(i)
