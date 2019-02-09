def generalizedGCD(num, arr):
    # WRITE YOUR CODE HERE
    mini = min(arr)

    for i in range(mini, -1, -1):
        for number in arr:
            if (number % i) != 0:
                break
        else:
            return i
    return 1


print(generalizedGCD(5, [2, 4, 6, 8, 10]))
