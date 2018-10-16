def move_zeros(arr):
    i = j = 0
    while i < len(arr):
        if arr[i] > 0:
            arr[j] = arr[i]
            j += 1
        i += 1

    while j < len(arr):
        arr[j] = 0
        j += 1

    return arr
