class Solution:
    def maxSum(self, nums: List[int]) -> int:
        
        arr=[]

        for i in nums:
            if i not in arr:
                arr.append(i)
        
        arr.sort()

        while len(arr)!=1:
            if arr[0]>=0:
                break
            if arr[0] < 0:
                arr.pop(0)
        return sum(arr)



        
