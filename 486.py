class Solution:
    def predictTheWinner(self, arr: List[int]) -> bool:
        n=len(arr)

        def game(arr,i,j,points, p1):

            if i>j:
                return points

            if p1:
                a=game(arr,i+1,j,points+arr[i],False)
                b=game(arr,i,j-1,points+arr[j],False)
            else:
    
                a=game(arr,i+1,j,points,True)
                
                b=game(arr,i,j-1,points,True)

                return min(a,b)
                
            return max(a,b)


        player1=(game(arr,0,n-1,0,True))
        player2=sum(arr)-player1

        if player1>=player2:
            return True
        else:
            return False

        
        
