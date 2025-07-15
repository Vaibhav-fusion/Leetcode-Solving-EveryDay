class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        if word.isalnum()==False:
            return False
        s=['a','e','i','o','u','A','E','I','O','U']

        check1=False
        check2=False

        for i in word:
            if i in s:
                check1=True
            else:
                if i.isalpha():
                    check2=True 

        if check1==False or check2==False:
            return False
        return True
