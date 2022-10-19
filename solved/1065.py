def is_han_soo(x:int):
    if x < 100:
        return "Yes"
    else:
        str_x = str(x)
        for i in range(1,len(str_x)):
            if (int(str_x[i-1]) - int(str_x[i])) != (int(str_x[i]) - int(str_x[i+1])):
                return "No"
                break
            else:
                return "Yes"

han_soo_count = 0

N = int(input())

for i in range(1,N+1):
    if is_han_soo(i) == "Yes":
        han_soo_count += 1

print(han_soo_count)
