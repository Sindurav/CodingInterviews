def fourSum(arr, s):
    arr = [[i, arr[i]] for i in range(len(arr))]
    arr = sorted(arr, key=lambda x:x[1])
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            k = j+1
            l = len(arr)-1
            while k < l:
                four_sum = arr[i][1]+arr[j][1]+arr[k][1]+arr[l][1]
                if four_sum == s:
                    return sorted([arr[i][0], arr[j][0], arr[k][0], arr[l][0]])
                elif four_sum < s:
                    k += 1
                else:
                    l -= 1

    return []


array = [2, 7, 4, 0, 9, 5, 1, 3]
target = 20
result = fourSum(array, target)
print(result)
