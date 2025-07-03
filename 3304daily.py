class Solution:
    def kthCharacter(self, k: int) -> str:

        def fun(s):

            new=''

            for i in s:
                if i=='z':
                    new+='a'
                else:
                    new+=chr(ord(i)+1)
            
            return s+new
        
        og='a'
        while len(og)<k:
            og=fun(og)
        print(og)
        return og[k-1]




        
