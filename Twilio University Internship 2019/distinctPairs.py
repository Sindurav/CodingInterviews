def numberOfPairs(nums, target):
    if len(nums) <= 1:
        return 0

    distinct_pairs = set([])
    nums = sorted(nums)

    for i, num in enumerate(nums):
        search_res = binary_search(nums, i, len(nums) - 1, target - nums[i])
        if search_res != -1:
            distinct_pairs.add(tuple(sorted([num, search_res])))
    return len(distinct_pairs)


def binary_search(arr, l, r, x):
    idx = l
    while r >= l:
        mid = (l + r) // 2

        if arr[mid] == x:
            if mid != idx:
                return arr[mid]
            else:
                if arr[mid - 1] == x or arr[mid + 1] == x:
                    return arr[mid]
                else:
                    return -1
        elif arr[mid] > x:
            r = mid - 1
        else:
            l = mid + 1

    return -1
