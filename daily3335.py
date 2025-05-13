class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        d={}

        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1

        for i in range(t):
            w={}
            for key in d:
                if key < 'z':
                    temp=ord(key)
                    new_key=chr(temp+1)
                    if new_key in w:
                        w[new_key]+=d[key]
                    else:
                        w[new_key]=d[key]
                if key=='z':

                    if 'a' in w:
                        w['a']+=d[key]
                    else:
                        w['a']=d[key]

                    if 'b' in w:
                        w['b']+=d[key]
                    else:
                        w['b']=d[key]
                        


                    
            d=w.copy()

        return (sum(d.values())%(10**9+7))
        
