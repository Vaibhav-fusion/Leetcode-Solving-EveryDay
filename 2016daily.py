class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans=-1
        n=len(nums)
        pre=[0]*n
        pre[-1]=nums[-1]
        for i in range(n-2,-1,-1):
            pre[i]=max(nums[i],pre[i+1])
        # print(pre)
        # print(nums)
        for i in range(0,n-1):
            ans=max(ans,(pre[i+1]-nums[i]))
            print(ans,pre[i+1],nums[i],end=" ")
            print()

        if ans==0:
            return -1
        else:
            return ans

            
            
