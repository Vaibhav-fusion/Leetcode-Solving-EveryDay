class Solution:
    def partitionArray(self, arr: List[int], k: int) -> int:
        n=len(arr)

        # if k==0:
        #     return n-1
        arr.sort()
        ans=0
        i=0
        
        for j in range(0,n):
            if arr[j]-arr[i]>k:
                ans+=1
                i=j
        print(arr,i)
        return ans+1



            



        
