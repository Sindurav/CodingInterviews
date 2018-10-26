#
# Complete the 'maxLength' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#


def maxLength(a, k):
    # Write your code here
    summ = count = max_count = 0
    for i in range(len(a)):
        if k >= summ+a[i]:
            summ += a[i]
            count += 1
        elif summ != 0:
            summ = summ - a[i-count] + a[i]
        max_count = max(count, max_count)
    return max_count
