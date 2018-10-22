def triplets(arr, t):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if j == i:
                continue
            for k in range(len(arr)):
                if k != j and k != i and arr[i] + arr[j] + arr[k] <= t:
                    count += 1
    return count
