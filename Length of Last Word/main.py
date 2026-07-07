class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cuvinte = s.split()
        
        return len(cuvinte[-1])
        