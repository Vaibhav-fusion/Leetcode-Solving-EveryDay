class Solution:
    def maximum69Number (self, num: int) -> int:

        s = str(num)
        res=''
        state=True



        for i in range(len(s)):

            if s[i]=='6' and state==True:
                res+='9'
                state=False
                
            else:
                res+=s[i]

        return int(res)

        
