arr = [0, 1, 0, 3, 12]

done=0

for i in range(len(arr)):
    if arr[i]!=0:
        arr[done],arr[i]=arr[i],arr[done]
        done+=1
print(arr)