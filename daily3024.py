class Solution:
    def triangleType(self, s: List[int]) -> str:

        a,b,c=s[0],s[1],s[2]

        if not (a + b > c and a + c > b and b + c > a):
            return 'none'



        if s[0]==s[1]==s[2]:
            return "equilateral"
        
        if s[1]==s[2] or s[0]==s[1] or s[0]==s[2]:
            return "isosceles"
        
        return "scalene"
        
