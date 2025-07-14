# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        trav=head
        res=''
        while trav:
            res+=str(trav.val)
            trav=trav.next 

        if res=='':
            return 0

        ans=0
        lenght=len(res)-1
        for i in res:
            ans+=int(i)*(2**lenght)
            lenght-=1
        return ans

        return res
        
