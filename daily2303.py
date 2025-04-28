class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        pre = [nums[0]]
        for i in range(1,n):
            pre.append(pre[-1]+nums[i])

        ans = 0

        i = 0
        j = 0

        while j<n:
            if i==0:
                x = pre[j]
            else:
                x = pre[j] - pre[i-1]

            while i <= j and x * (j-i+1) >= k:
                i += 1
                if i == 0:
                    x = pre[j]
                else:
                    x = pre[j] - pre[i-1]
            
            ans += (j - i + 1)
            j += 1

        return(ans)
