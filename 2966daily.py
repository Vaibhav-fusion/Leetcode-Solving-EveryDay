class Solution:
    def divideArray(self, arr: List[int], k: int) -> List[List[int]]:
        arr.sort()

        n=len(arr)

        ans=[]
        for i in range(0,n,3):

            a=arr[i]
            b=arr[i+1]
            c=arr[i+2]

            if abs(a-b)<=k and abs(a-c)<=k and abs(b-c)<=k:
                ans.append([a,b,c])
            else:
                return []
        return ans

        

        
