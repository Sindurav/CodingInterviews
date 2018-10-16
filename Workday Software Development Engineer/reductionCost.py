#
# Complete the 'reductionCost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY num as parameters:


def reductionCost(nums):
    summ = 0
    while len(num) != 0:
        num = sorted(num)
        summ += num[0]+num[1]
        num = [num[0]+num[1]+num[2:]]
    return summ