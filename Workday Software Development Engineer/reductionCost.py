#
# Complete the 'reductionCost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY num as parameters:


def reductionCost(nums):
    summ = 0
    while len(nums) != 0:
        nums = sorted(nums)
        summ += nums[0]+nums[1]
        nums = [nums[0]+nums[1]+nums[2:]]
    return summ
