def solution(A):
    # write your code in Python 3.6
    tot_count = 0
    maxi = max(A)
    # print("maxi", maxi)
    for i in range(1, maxi+1):
        count = 0
        continuous = True
        for j in range(len(A)):
            if A[j]>=i:
                if continuous == False or count == 0:
                    count += 1
                    continuous = True
            elif A[j]<i:
                continuous = False
        # print("count=", count)
        tot_count += count
    return tot_count
