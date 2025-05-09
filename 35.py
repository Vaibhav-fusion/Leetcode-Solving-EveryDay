class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ans=-1


        i=0
        j=len(nums)-1

        while i<=j:
            
            mid=(i+j)//2

            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                j=mid-1
            else:
                i=mid+1
        
        return max(i,j)


