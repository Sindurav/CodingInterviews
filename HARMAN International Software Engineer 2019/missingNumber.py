def missing_number(nums):
    arr = [0 for _ in range(len(nums))]

    for i in range(len(nums)):
        if nums[i] < len(nums):
            arr[nums[i]] = -1

    for i in range(len(nums)):
        if arr[i] != -1:
            return i

    return len(nums)