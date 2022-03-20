def Lowerindex(arr,target):
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]>=target:
            high=mid-1
        else:
            low=mid+1
    return low

def Upperindex(arr,target):
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]<=target:
            low=mid+1
        else:
            high=mid-1
    return high






target=int(input())
arr=[int(i) for i in input().split()]
x=Lowerindex(arr,target)
y=Upperindex(arr,target)
d=[]
for i in range(x,y+1):
    if arr[i]==target:
        d.append(i)
print(d)
        
    
