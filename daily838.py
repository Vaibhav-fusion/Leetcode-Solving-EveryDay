class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)

        if dominoes[0]=="." or dominoes[0]=="L":
            pre_R = [0]
        else:
            pre_R = [n]

        if dominoes[-1]=="." or dominoes[-1]=="R":
            suff_L = [0]
        else:
            suff_L = [n]

        for i in range(1,n):
            if dominoes[i]==".":
                pre_R.append(pre_R[-1]-1 if pre_R[-1]-1>0 else 0)
            elif dominoes[i]=="R":
                pre_R.append(n)
            else:
                pre_R.append(0)

        for i in range(n-2,-1,-1):
            if dominoes[i]==".":
                suff_L.append(suff_L[-1]-1 if suff_L[-1]-1>0 else 0)
            elif dominoes[i]=="R":
                suff_L.append(0)
            else:
                suff_L.append(n)

        suff_L.reverse()

        ans = ""

        for i in range(n):
            if pre_R[i]-suff_L[i]==0:
                ans+="."
            elif pre_R[i]-suff_L[i]>0:
                ans+="R"
            else:
                ans+="L"

        return(ans)
