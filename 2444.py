class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        def myCode(minK, maxK, nums):
            if not nums:
                return 0

            if len(nums) == 1:
                if minK == nums[0] == maxK:
                    return 1
                else:
                    return 0

            i = 0
            min_pos = -1
            max_pos = -1
            ans = 0

            while i < len(nums):
                if nums[i] == minK:
                    min_pos = i
                if nums[i] == maxK:
                    max_pos = i

                if min_pos != -1 and max_pos != -1:
                    ans += min(min_pos, max_pos) + 1

                i += 1

            return ans

        total = 0
        l = []

        if minK > maxK:
            return(0)
        else:
            for i in range(len(nums)):
                if minK <= nums[i] <= maxK:
                    l.append(nums[i])
                else:
                    if l:
                        total += myCode(minK, maxK, l)
                        l = []
                if i == len(nums) - 1 and l:
                    total += myCode(minK, maxK, l)

            return(total)
