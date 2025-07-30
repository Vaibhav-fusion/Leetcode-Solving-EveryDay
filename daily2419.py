class Solution:
    def longestSubarray(self,arr: List[int]) -> int:
        n=len(arr)

        Max=max(arr)

        cur=0
        mox=0
        for i in arr:

            if i==Max:
                cur+=1
            else:
                cur=0
            mox=max(cur,mox)
        return mox


        
