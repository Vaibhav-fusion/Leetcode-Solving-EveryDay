class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        count = 0
        d = {0: 1}
        ans = 0

        for i in range(len(nums)):
            if nums[i] % modulo == k:
                count += 1

            target = (count - k) % modulo
            if target in d:
                ans += d[target]
                  

            x = count % modulo
            if x in d:
                d[x] += 1
            else:
                d[x] = 1

        return(ans)
