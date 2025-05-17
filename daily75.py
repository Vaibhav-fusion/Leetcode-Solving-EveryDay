class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        d={0:0,1:0,2:0}

        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1

        
        for i in range(len(nums)):
            if d[0]>0:
                nums[i]=0
                d[0]-=1
                continue
            if d[1]>0:a
                nums[i]=1
                d[1]-=1

                continue
            if d[2]>0:
                nums[i]=2
                d[2]-=1
                
                continue

        return nums

        
        
