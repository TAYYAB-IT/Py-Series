def Binary_Search():
    arr=[2,3,4,5,6,7,8,9]
    lb=0
    ub=len(arr)-1
    s=90
    mid=(lb+ub)//2
    while(ub!=mid):

     if(s>arr[mid]):
        lb=mid+1
     else:
            ub=mid
     mid=(lb+ub)//2
    if(arr[mid]==s):
        print('Found at ',mid)
    else:
        print("Not Found")
    return

#Binary_Search()
def Selection_Sorting():
    arr=[3,2,1,4,6,7,345,221,5,100,]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i])>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    
    print("Seletion_ Sorted:: ",arr)
#Selection_Sorting()
def Bubble_Sorting():
    arr=[9,67,53,24,3,2,5,3,76,8]
    print(arr)
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
        print(arr)
x=Bubble_Sorting()
