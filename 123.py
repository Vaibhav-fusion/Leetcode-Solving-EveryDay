class Solution:
    def maxProfit(self, arr: List[int]) -> int:

            n=len(arr)

            pre_prof=[0]*n

            cur=0
            max_profit=0
            Max=0

            for i in range(n-1,-1,-1):
                Max=max(Max,arr[i])
                cur=Max-arr[i]
                
                max_profit=max(max_profit,cur)
                pre_prof[i]=max_profit

            # print(pre_prof)

            final=pre_prof[0] 

            cur=0
            max_profit=0
            Min=float('inf')

            for i in range(n-2):
                Min=min(Min,arr[i])
                cur=arr[i]-Min 
                max_profit=max(max_profit,cur)
                final=max(final,max_profit+pre_prof[i+1])
            return final
            






        
