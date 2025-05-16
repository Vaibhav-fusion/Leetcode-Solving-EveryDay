import sys 
sys.setrecursionlimit(10**6)
class Solution:
    def getWordsInLongestSubsequence(self, arr: List[str], grp: List[int]) -> List[str]:

        dp={}

        def humming_bird(a,b):
            if len(a)!=len(b):
                return False

            res=0
            for i in range(len(a)):
                if a[i]!=b[i]:
                    res+=1
                
            if res==1:
                return True
            return False


        ans=[]
        n=len(arr)
        def helper(arr,grp,i,prev,prev_word,dp):

            if (i,prev_word) in dp:
                return dp[(i,prev_word)]

            if i==n:
                return []

            if prev==None:
                
                option1=[arr[i]]+helper(arr,grp,i+1,grp[i],arr[i],dp)

                option2=helper(arr,grp,i+1,prev,prev_word,dp)

                # print(option1,option2)

                if len(option1)>len(option2):
                    dp[(i,prev_word)]=option1
                    return option1
                else:
                    dp[(i,prev_word)]=option2

                    return option2


            if grp[i]==prev:

                store= helper(arr,grp,i+1,prev,prev_word,dp)
                dp[(i,prev_word)]=store
                return store


            if humming_bird(arr[i],prev_word):
                option1=[arr[i]]+helper(arr,grp,i+1,grp[i],arr[i],dp)

                option2=helper(arr,grp,i+1,prev,prev_word,dp)

                if len(option1)>len(option2):
                    dp[(i,prev_word)]=option1

                    return option1
                else:
                    dp[(i,prev_word)]=option2

                    return option2
                
            else:

                dp[(i,prev_word)] =helper(arr,grp,i+1,prev,prev_word,dp)
                return dp[(i,prev_word)] 
                
                    


        return(helper(arr,grp,0,None,None,dp))
