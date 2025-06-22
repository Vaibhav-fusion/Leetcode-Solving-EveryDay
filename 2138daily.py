class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:

        res=[]
        n=len(s)

        for i in range(0,len(s),k):
            temp=s[i:i+k]
            if len(temp)==k:
                res.append(temp)
            else:

                while len(temp)<k:
                    temp+=fill
                res.append(temp)

        return res
        
