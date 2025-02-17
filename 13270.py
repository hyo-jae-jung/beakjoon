import sys 

N = int(sys.stdin.readline().strip())
memo = {0:0,1:1}

a,b,c = 0,1,2
while c < N:
    memo.update({c:memo[a]+memo[b]})
    a = b
    b = c
    c = a + b

memo.pop(1)
memo.pop(0)

def subset_sum_with_duplicates_unique(nums, target):
    dp = set()
    dp.add(())

    for _ in range(target):
        new_combinations = set()
        for combination in dp:
            for num in nums:
                new_sum = sum(combination) + num
                if new_sum <= target:
                    new_combination = tuple(sorted(combination + (num,)))
                    new_combinations.add(new_combination)
        dp.update(new_combinations)

    result = [list(combo) for combo in dp if sum(combo) == target]
    return result

result = subset_sum_with_duplicates_unique(memo.keys(), N)
arr = set()
for i in result:
    tmp = 0
    for j in i:
        tmp+=memo[j]
    arr.add(tmp)

print(min(arr),max(arr))
