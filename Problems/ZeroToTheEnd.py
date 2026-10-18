arr=[0, 1, 0, 3, 12]
new_arr=[]
c=0
for i in arr:
    if i==0:
        c+=1
    else:
        new_arr.append(i)
for i in range(c):
    new_arr.append(0)

print(new_arr)