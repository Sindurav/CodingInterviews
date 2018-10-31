#
# Complete the 'flowerBouquets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
# 1. INTEGER p
# 2. INTEGER q
# 3. STRING s
#


def findMaxProfit(jobs):
    tabulation = []
    for i in range(len(jobs)):
        tabulation.append(jobs[i][2])
    for i in range(len(jobs)):
        for j in range(i + 1, len(jobs)):
            if jobs[i][1] < jobs[j][0]:
                tabulation[j] = max(tabulation[j], jobs[j][2] + tabulation[i])
    return tabulation[-1]


def flowerBouquets(p, q, s):
    if len(s) <= 1:
        return 0
    jobs = []
    type1 = "000"

    for i in range(len(s)):
        if s[i:i + 3] == type1:
            jobs.append([i, i + 2, p])
        else:
            cur = s[i: i + 2]
            if cur == "01" or cur == "10":
                jobs.append([i, i + 1, q])
    if not jobs:
        return 0
    return findMaxProfit(jobs)
