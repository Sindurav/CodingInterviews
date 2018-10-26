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


def tripletsSorting(arr, t):
    count = 0
    arr = sorted(arr)
    results = []
    for i in range(len(arr)):
        if arr[i] >= t:
            break
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] >= t:
                break
            for k in range(j+1, len(arr)):
                currentSum = arr[i] + arr[j] + arr[k]
                if currentSum <= t:
                    results.append([arr[i], arr[j], arr[k]])
                    count += 1
                else:
                    break
    print("results =", results)
    return count
