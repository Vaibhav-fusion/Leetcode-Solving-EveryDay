class Solution:
    def maxDifference(self, s: str) -> int:
        d={}

        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        odd=[]
        even=[]

        for i in d:
            if d[i]%2==0:
                even.append(d[i])
            else:
                odd.append(d[i])
        
        diff=float('-inf')

        for i in odd:
            for j in even:
                diff=max((i-j),diff)

        return diff


        
