#
# Complete the 'reductionCost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY num as parameters:


def reductionCost(nums):
    # You can also solve this by heap data-structure
    # Since this submission got accepted by Hackerrank so I did not use heap
    summ = 0
    while len(nums) != 0:
        nums = sorted(nums)
        summ += nums[0]+nums[1]
        nums = [nums[0]+nums[1]+nums[2:]]
    return summ
