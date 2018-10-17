#
# Complete the 'degreeOfArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
from collections import Counter, defaultdict


def degreeOfArray(arr):
    # Write your code here
    maxDeg = 0
    num2count = defaultdict(int)
    firstSeen = {}
    lastSeen = {}
    for idx, num in enumerate(arr):
        num2count[num] += 1
        if num not in firstSeen:
            firstSeen[num] = idx
        lastSeen[num] = idx

        maxDeg = max(maxDeg, num2count[num])

    minLength = float("inf")
    for num in num2count:
        if num2count[num] == maxDeg:
            minLength = min(minLength, (lastSeen[num] - firstSeen[num]))

    return minLength + 1