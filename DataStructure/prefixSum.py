arr=[1,2,3,4,5,6,7,8]
r=len(arr)-1

prefixSum=[0]*r
prevSum=0
# arr.append(1)
print(arr)
for i in range(r):
    prefixSum[i]=prevSum+arr[i]
    prevSum=prefixSum[i]

print(prefixSum)


