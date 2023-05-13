nums = [-1,-2]

"""max_sum = min(nums)
max_num = []

for i in range(1, len(nums) + 1):
    for j in range(0, len(nums)):
        # print(j, i)
        if sum(nums[j:i+1:]) > max_sum:
            # print(nums[j:i:])
            max_sum = sum(nums[j:i+1:])
            # print(max_sum)
            max_num = nums[j:i+1:]
            print(max_num)

        else:
            pass


print(max_sum)
# print(max_num)
"""

max_sum = nums[0]
cur_sum = 0

for num in nums:
    if cur_sum < 0:
        cur_sum = 0
    cur_sum += num
    max_sum = max(max_sum, cur_sum)


print(max_sum)