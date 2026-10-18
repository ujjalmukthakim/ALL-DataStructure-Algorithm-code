arr=[3, 1, 3, 2, 1, 5]
arr_new=[]

for i in arr:
    if i in arr_new:
        continue
    else:
        arr_new.append(i)
print(arr_new)