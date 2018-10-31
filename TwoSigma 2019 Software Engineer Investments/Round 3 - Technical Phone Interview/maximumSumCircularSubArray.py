# Time Complexity - O(n^2)
# Space Complexity - O(n)
# Better solutions out there with O(n) solution


def apply_kadenze(arr):
    max_so_far = arr[0]
    max_ending = arr[0]
    for i in range(1, len(arr)):
        max_ending = max(arr[i], max_ending + arr[i])
        max_so_far = max(max_so_far, max_ending)
    return max_so_far


def find_max_sub_array(arr):
    if not arr:
        return 0

    if len(arr) == 1:
        return arr[0]

    global_max = apply_kadenze(arr)
    for i in range(len(arr)):  # every element
        arr = [arr[-1]] + arr[0:-1]  # Operation not needed if its a linked list
        cur_max = apply_kadenze(arr)
        global_max = max(global_max, cur_max)

    return global_max


array = [-1, 2, 4, -1]
result = find_max_sub_array(array)
print("results =", result)

array = [5, -1, 4, 1]
result = find_max_sub_array(array)
print("results =", result)

array = [10, -1, 2, 3, 4, 5]
result = find_max_sub_array(array)
print("results =", result)

array = []
result = find_max_sub_array(array)
print("results =", result)

array = [-2]
result = find_max_sub_array(array)
print("results =", result)

