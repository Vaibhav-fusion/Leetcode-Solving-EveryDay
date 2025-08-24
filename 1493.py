class Solution:
    def longestSubarray(self, arr: List[int]) -> int:

        if (arr.count(0) == len(arr)):
            return 0

        i=0
        j=0
        d={0:0,1:0}
        res=0
        n=len(arr)
        print(n)

        while j<=n-1:

            if d[0]<=1:
                d[arr[j]]+=1
                if d[0]<=1:

                    res= max(res, d[0]+d[1]-1)
                j+=1
            
            else:
                d[arr[i]]-=1
                i+=1
                if d[0]<=1:
                    res= max(res,d[0]+ d[1]-1)
                    
        


            print(i,j,d,res)

        return res

    



        
