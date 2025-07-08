class Solution:
    def transpose(self, arr: List[List[int]]) -> List[List[int]]:
        
        n=len(arr)
        m=len(arr[0])

        res=[[0]*n for i in range(m)]

        for i in range(m):
            for j in range(n):
                res[i][j]=arr[j][i]

        return res
