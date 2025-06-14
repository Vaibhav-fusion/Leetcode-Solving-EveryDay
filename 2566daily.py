class Solution:
    def minMaxDifference(self, num: int) -> int:
        digit=None 

        for i in str(num):
            if digit is not None:
                break
            if i!='9':
                digit=i

        
        s=str(num)

        if digit==None:
            new_s=num

        else:
            new_s=''
            for i in s:
                if i==digit:
                    new_s+='9'
                else:
                    new_s+=i

        digit=None
        for i in s:
            if digit is not None:
                break
            if i!='0':
                digit=i
        if digit==None:
            new_p=num
        else:
            new_p=''
            for i in s:
                if i==digit:
                    new_p+='0'
                else:
                    new_p+=i
        
    
        return int(new_s)-int(new_p)

        


