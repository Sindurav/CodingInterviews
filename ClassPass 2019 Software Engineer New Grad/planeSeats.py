def solve(n, s):
    seats1 = ["A", "B", "C"]
    seats2 = ["D", "E", "F", "G"]
    seats3 = ["J", "L", "I"]

    s_list = s.plit()
    reserved = set([])
    for i in range(len(s_list)):
        reserved.add(s_list[i])

    count = 0
    for i in range(1, n + 1):
        num = str(i)
        if (num+seats1[0] not in reserved) and (num+seats1[1] not in reserved) and (num+seats1[2] not in reserved):
            count += 1

        if (num+seats3[0] not in reserved) and (num+seats3[1] not in reserved) and (num+seats3[2] not in reserved):
            count += 1

        if (num+seats2[0] not in reserved) and (num+seats2[1] not in reserved) and (num+seats2[2] not in reserved):
            count += 1
        elif (num+seats2[1] not in reserved) and (num+seats2[2] not in reserved) and (num+seats2[3] not in reserved):
            count += 1

    return count
