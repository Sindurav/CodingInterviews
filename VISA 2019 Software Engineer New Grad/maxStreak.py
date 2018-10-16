#
# Complete the 'maxStreak' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
# 1. INTEGER m
# 2. STRING_ARRAY data
#

def maxStreak(m, data):
    # Write your code here
	curStreak = maxStreak = 0
    for day in data:
        for i in range(m):
            if day[i] != "Y":
		curStreak = 0
                break
	else:
	    curStreak += 1		
	maxStreak = max(maxStreak, curStreak)
    
    return maxStreak