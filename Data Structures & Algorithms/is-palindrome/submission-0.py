class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1=str.copy()
        str1.reverse()
        if str1==str:
            return True
        else:
            return False
