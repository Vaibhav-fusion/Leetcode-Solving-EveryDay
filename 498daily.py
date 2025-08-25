class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        res = []

        n,m=len(mat),len(mat[0])

        toggle = False

        for j in range(m):

            left,right = 0,j

            cur = []

            while (left<n and left>=0 )and right>=0:

                cur.append(mat[left][right])
                left+=1
                right-=1

            if toggle:
                res.extend(cur)
            else:
                res.extend(cur[::-1])
            toggle= not (toggle)
        
        for i in range(1,n):
            left,right = i , m-1
            cur = []

            while (left<n and left>=0 )and right>=0:

                cur.append(mat[left][right])
                left+=1
                right-=1

            if toggle:
                res.extend(cur)
            else:
                res.extend(cur[::-1])
            toggle= not (toggle)



        return res


        
