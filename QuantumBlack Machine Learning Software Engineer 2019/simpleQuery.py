# Complete the counts function below.
def bin_search(arr, target):
    left, ryt = 0, len(arr)-1
    while left<len(arr) and ryt>= 0 and left<=ryt:
        mid = (left+ryt)//2
        if arr[mid] == target:
            return mid+1
        elif arr[mid]>target:
            ryt = mid-1
        else:
            left = mid+1
    return left

def counts(nums, maxs):
    nums = sorted(nums)
    results = []
    for maxi in maxs:
        count = bin_search(nums, maxi)
        results.append(count)
    return results    


arr = [1, 2, 4, 4, 7]
maxes = [3, 5]
res = counts(arr, maxes)
print("numbers =", arr, "maxes =", maxes, "answer =", res)

arr = [2, 10, 5, 4, 8]
maxes = [3, 1, 7, 8]
res = counts(arr, maxes)
print("numbers =", arr, "maxes =", maxes, "answer =", res)

arr = [1, 4, 2, 4]
maxes = [3, 5]
res = counts(arr, maxes)
print("numbers =", arr, "maxes =", maxes, "answer =", res)
