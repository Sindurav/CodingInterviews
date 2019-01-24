def solution(A):
    # write your code in Python 3.6
    newA = [[i, A[i]] for i in range(len(A))]
    newA = sorted(newA, key=lambda x: x[1], reverse=True)

    max_dist = 0
    for i in range(len(newA)):
        for j in range(len(newA)):
            dist = newA[i][1] + newA[j][1] + abs(newA[j][0] - newA[i][0])
            max_dist = max(max_dist, dist)
    return max_dist
