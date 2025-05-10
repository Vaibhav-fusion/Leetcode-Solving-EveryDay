class Solution:
    def minSum(self, arr1: List[int], arr2: List[int]) -> int:
        
        d1 = 0
        brr1 = []
        for x in arr1:
            if x == 0:
                brr1.append(1)
                d1 += 1
            else:
                brr1.append(x)
        
        d2 = 0
        brr2 = []
        for x in arr2:
            if x == 0:
                brr2.append(1)
                d2 += 1
            else:
                brr2.append(x)

        cal1 = sum(brr1)
        cal2 = sum(brr2)

        if cal1 == cal2:
            return cal1
        
        if cal1 > cal2:
            return cal1 if d2 > 0 else -1
        else:
            return cal2 if d1 > 0 else -1
