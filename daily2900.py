class Solution:
    def getLongestSubsequence(self, words: List[str], brr: List[int]) -> List[str]:
        
        ans=[]
        ans.append(words[0])
        prev=0
        n=len(words)
        for i in range(1,n):
            if brr[i]!=brr[prev]:
                ans.append(words[i])
                prev=i

        return ans


        
