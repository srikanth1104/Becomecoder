class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums==[] or target not in nums:
            return -1,-1
        def Lowerindex(nums,target):
            low=0
            high=len(nums)-1
            while(low<=high):
                mid=(low+high)//2
                if nums[mid]>=target:
                    high=mid-1
                else:
                    low=mid+1
            return low
        def Upperindex(arr,target):
            low=0
            high=len(arr)-1
            while(low<=high):
                mid=(low+high)//2
                if nums[mid]<=target:
                    low=mid+1
                else:
                    high=mid-1
            return high
        x=Lowerindex(nums,target)
        y=Upperindex(nums,target)
        if nums[x]==target and nums[y]==target:
            return x,y
                
