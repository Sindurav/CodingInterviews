def kSub(k, arr):
    n = len(arr)
    mod = [0 for _ in range(k + 1)]
    result = cumSum = 0

    for i in range(n):
        cumSum = cumSum + arr[i]
        mod[((cumSum % k) + k) % k] = mod[((cumSum % k) + k) % k] + 1

    for i in range(k):
        if mod[i] > 1:
            result = result + (mod[i] * (mod[i] - 1)) // 2

    return result + mod[0]
