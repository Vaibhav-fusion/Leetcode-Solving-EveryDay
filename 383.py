class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag={}

        for i in magazine:
            if i in mag:
                mag[i]+=1
            else:
                mag[i]=1

        for i in ransomNote:
            if i not in mag:
                return False
            else:
                if mag[i]>0:
                    mag[i]-=1
                else:
                    return False

        return True
        
