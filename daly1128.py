class Solution:
    def numEquivDominoPairs(self, arr: List[List[int]]) -> int:

        seen={}

        ans=0

        for i in arr:

            tup=(i[0],i[1])
            inv_tup=(i[1],i[0])

            if inv_tup in seen:
                seen[inv_tup]+=1

            elif tup in seen:
                seen[tup]+=1
            else:
                seen[tup]=1

        for i in seen:
            ans+= seen[i]*(seen[i]-1)//2
            

        return ans





        
