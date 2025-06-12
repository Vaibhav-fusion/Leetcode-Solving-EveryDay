class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:

        diff=float('-inf')

        for i in range(len(nums)):
            if i==len(nums)-1:
                cur=abs(nums[i]-nums[0])
            else:
                cur=abs(nums[i]-nums[i+1])

            diff=max(diff,cur)

        return diff
        
