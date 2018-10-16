def find_idx(sorted_arr, target):
    length = len(sorted_arr)
    left = 0
    right = length-1
    while (left <= right) and (right >= 0) and (left < length):

        middle = (left+right)//2
        if sorted_arr[middle] == target:

            return middle

        elif sorted_arr[middle] < target:
            left = middle+1
        else:
            right = middle-1

    return left
