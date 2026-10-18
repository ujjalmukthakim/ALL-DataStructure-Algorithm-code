arr = [12, 5, 37, 9, 21]
largest=arr[0]
for i in range(len(arr)):
    if largest<arr[i]:
        largest=arr[i]

print(largest)
