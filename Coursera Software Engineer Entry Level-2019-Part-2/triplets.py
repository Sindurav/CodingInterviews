def bin_search(arr, target, start):
    left, ryt = start, len(arr)-1
    while left<len(arr) and ryt >= start and left <= ryt:
        mid = (left+ryt)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            ryt = mid-1
        else:
            left = mid+1
    return left


def tripletsSorting(nums, t):
    # TimeComplexity = O((n^2)logn)
    nums.sort()
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            target = t - nums[i] - nums[j]
            if target < 0:
                break
            k = bin_search(nums, target, j+1)
            if k < len(nums) and nums[k] <= target:
                count += (k-j)
            elif k <= len(nums):
                count += (k-j-1)
    print(count)
    return count


def triplets(arr, t):
    # TimeComplexity = O((n^3))
    count = 0
    sets = set([])
    for i in range(len(arr)):
        for j in range(len(arr)):
            if j == i:
                continue
            for k in range(len(arr)):
                if k == j or k == i or i == j:
                    continue
                summ = (arr[i] + arr[j] + arr[k])
                if frozenset((arr[i], arr[j], arr[k])) not in sets and summ <= t:
                    sets.add(frozenset((arr[i], arr[j], arr[k])))
                    count += 1
    print(count)
    return count


def tripletsSortWithPruning(arr, t):
    # TimeComplexity = O((n^3))
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
    print(count)
    return count


array = [1, 2, 3, 4, 5]
threshold = 8
tripletsSorting(array, threshold)
triplets(array, threshold)
tripletsSortWithPruning(array, threshold)
print("============")

array = [1, 2, 3, 4, 6, 9]
threshold = 8
tripletsSorting(array, threshold)
triplets(array, threshold)
tripletsSortWithPruning(array, threshold)
print("============")


array = [1, 2, 3, 4, 6, 5]
threshold = 11
tripletsSorting(array, threshold)
triplets(array, threshold)
tripletsSortWithPruning(array, threshold)
print("============")
