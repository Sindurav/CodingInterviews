def numberOfPaths(mat):
    # Write your code here
    tabulation = [[0] * len(mat[0]) for i in mat]

    if mat[0][0] == 1: tabulation[0][0] = 1

    for i in range(1, len(mat)):
        if mat[i][0] == 1:
            tabulation[i][0] = tabulation[i - 1][0]

    for j in range(1, len(mat[0])):
        if mat[0][j] == 1:
            tabulation[0][j] = tabulation[0][j - 1]

    for i in range(1, len(mat)):
        for j in range(1, len(mat[0])):
            if mat[i][j] == 1:
                tabulation[i][j] = tabulation[i - 1][j] + tabulation[i][j - 1]

    return tabulation[-1][-1] % (10 ** 9 + 7)
