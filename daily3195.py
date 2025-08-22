class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        check=False
        n=len(grid)
        m=len(grid[0])
        top =[n,m]
        bottom=[0,0]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    check =True
                    top[0] = min(top[0],i)
                    top[1] = min(top[1],j)

                    bottom[0]=max(bottom[0],i)
                    bottom[1]=max(bottom[1],j)

        if check:
            print(top,bottom)
            a= bottom[0]-top[0]+1
            b=bottom[1]-top[1]+1
            return a*b
        
        return 0






        
