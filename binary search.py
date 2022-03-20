target=int(input())
arr=[int(i) for i in input().split()]
start=0
end=len(arr)-1
while(start<=end):
    mid=(start+end)//2
    if arr[mid]==target:
        print('Found')
        break
    if arr[mid]<target:
        start=mid+1
    if arr[mid]>target:
        end=mid-1
else:
        print('Not found')







    
