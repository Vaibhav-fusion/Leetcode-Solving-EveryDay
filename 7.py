class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        check = False

        if x < 0:
            x = abs(x)
            check = True

        while x > 0:
            rev = rev * 10 + x % 10
            x = x // 10

        if check:
            rev = -rev

        if -2**31 <= rev <= 2**31 - 1:
            return rev
        else:
            return 0
