nums = [3, 0, 1]


def missing_number(n):
    num = len(n)
    for i in range(len(n)):
        num += (i - nums[i])

    return num


print(missing_number(nums))
