# 9
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        x = [i for i in str(x)]
        if x == x[::-1]:
            return True
        return False
