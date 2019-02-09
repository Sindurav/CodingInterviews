def generalizedGCD(num, arr):
    # WRITE YOUR CODE HERE
    mini = min(arr)

    for i in range(mini, -1, -1):
        for num in arr:
            if (num % i) != 0:
                break
        else:
            return i
    return 1
