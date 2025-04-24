class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        res=0

        total_distinct = len(set(nums))

        

        i = 0
        j = 0

        while j<n:
            x = len(set(nums[i:j+1]))

            if x>=total_distinct:
                res+= n-j
                i+=1
            else:
                j+=1

            if i>j:
                j=i

        return res
