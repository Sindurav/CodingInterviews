#
# Complete the 'missingWords' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#


def missingWords(s, t):
    # Write your code here
    s_list = s.split()
    t_list = t.split()
    missing = []
    i = j = 0
    while i < len(s_list) and j < len(t_list):
        if s_list[i] == t_list[j]:
            i += 1
            j += 1
        else:
            missing.append(s_list[i])
            i += 1

    for k in range(i, len(s_list)):
        missing.append(s_list[k])
    return missing
