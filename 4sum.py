

class Solution:
    def fourSum(self, arr: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(arr)

        flash = [[arr[i], i] for i in range(n)]
        flash.sort()  

        for i in range(n):
            for j in range(i + 1, n):
                required = target - flash[i][0] - flash[j][0]

               
                k = j + 1
                l = n - 1

                while k < l:
                    current = flash[k][0] + flash[l][0]
                    if current == required:
                        quad = [flash[i][0], flash[j][0], flash[k][0], flash[l][0]]
                        quad.sort()
                        if quad not in res:
                            res.append(quad)
                        k += 1
                        l -= 1
                    elif current < required:
                        k += 1
                    else:
                        l -= 1

        return res
