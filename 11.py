class Solution:
    def maxArea(self, arr: List[int]) -> int:
        # arr = [1,8,6,2,5,4,8,3,7]
# arr=[1,1]
        left=0
        right=len(arr)-1 

        ans=0
        while left<right:
            ans=max(ans , (min(arr[left],arr[right]))*(right-left) )

            if arr[left]<arr[right]:
                left+=1
            else:
                right-=1
        return ans 
        print(ans)


        
