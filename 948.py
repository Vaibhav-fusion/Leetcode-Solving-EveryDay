class Solution:
    def bagOfTokensScore(self, arr: List[int], power: int) -> int:

       

        # Your code here

        n=len(arr)

        score=0

        arr.sort()
        i,j=0,n-1

        while i<=j:
            # print(i,j,power)

            if arr[i]<=power:
                power-=arr[i]
                i+=1
                score+=1

            else:
                if score==0:
                    return 0
                if i!=j:
                    power+=arr[j]
                    j-=1
                    score-=1
                else:
                    break
            
            # print(score)

        return (score)
                
