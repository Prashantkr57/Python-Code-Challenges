nums = [-1,-1,0,-3,-3]

"""prod_nums = []

for i in range(len(nums)):
    prod = 1
    for j in range(len(nums)):

        if i == j:
            prod = prod * 1

        else:
            prod = prod * nums[j]

    prod_nums.append(prod)

print(prod_nums)
"""

res = [1] * (len(nums))

prefix = 1
for i in range(len(nums)):
    res[i] *= prefix
    prefix *= nums[i]

postfix = 1
for i in range(len(nums) - 1, -1, -1):
    res[i] *= postfix
    postfix *= nums[i]

print(res)