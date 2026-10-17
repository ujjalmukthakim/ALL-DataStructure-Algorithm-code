def max_subarray(arr):
    current = arr[0]
    best = arr[0]

    for i in range(1, len(arr)):
        current = max(arr[i], current + arr[i])
        best = max(best, current)

    return best

arr=[1,2,3,4,5,6,7]
a=max_subarray(arr)
print(a)