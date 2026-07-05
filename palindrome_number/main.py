class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        copie = x
        reverse = 0
        while copie > 0:
            reverse = (reverse * 10) + (copie % 10)
            copie = copie // 10
        return reverse == x