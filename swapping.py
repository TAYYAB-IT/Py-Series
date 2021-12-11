arr=[12,4,3,5,11,7,8]
for i in range(len(arr)//2):
    arr[i],arr[len(arr)-(i+1)]=arr[len(arr)-(i+1)],arr[i]
print(arr)