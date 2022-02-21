# import time as tm

# start = tm.time()

T = int(input())
N_list = [int(input()) for _ in range(T)]

class Memo(object):
    def __init__(self):
        self.memo = {}
        self.check = {0:0,1:0}
    def fibonacci(self, n:int) -> int:
        if n in [0,1]:
            self.check[n] += 1
            result = n
        # elif n in self.memo:
        #     result = self.memo[n]
        else:
            result = self.fibonacci(n-1) + self.fibonacci(n-2)
            # self.memo[n] = result
        return result

for i in N_list:
    a = Memo()
    a.fibonacci(i)
    print(a.check[0],a.check[1])
    


# end = tm.time()
# print(end-start)