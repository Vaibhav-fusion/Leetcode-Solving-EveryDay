class Solution:
    def maximumUniqueSubarray(self, arr: List[int]) -> int:
        i=0
        j=0

        mox=0
        cur=0
        d={}

        while i<=j and j<len(arr):

            if arr[j] not in d:
                cur+=arr[j]
                d[arr[j]]=1

                mox=max(mox,cur)
                j+=1

            else:
                cur-=arr[i]
                
                del d[arr[i]]

                i+=1
                
        return mox
        
