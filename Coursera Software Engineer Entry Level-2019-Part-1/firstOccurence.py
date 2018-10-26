#
# Complete the 'firstOccurrence' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING x
#


def firstOccurrence(s, x):
    # Write your code here
    xi = 0
    for idx, char in enumerate(s):
        if x[xi] == "*" or char == x[xi]:
            xi += 1
            if xi == len(x):
                return idx-len(x)+1
        else:
            xi = 0
    return -1
