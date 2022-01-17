def maximum(arr,n):
    max=arr[0]
    for i in range(1,n):
        if arr[i]>max:
            max=arr[i]
    return max
def minimum(arr,n):
    min=arr[0]
    for i in range(1,n):
        if arr[i]<min:
            min=arr[i]
    return min
arr=[25,234,80,60,20,348,32,1,90]
n=len(arr)
print("the maximum number is:",maximum(arr,n))
print("the minimum number is:",minimum(arr,n))