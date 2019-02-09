def generalizedGCD(num, arr):
    # WRITE YOUR CODE HERE
    arr = sorted(arr)

    for i in range(arr[0], -1, -1):
        for num in arr:
            if num%i != 0:
                break
        else:
            return i
    return 1
