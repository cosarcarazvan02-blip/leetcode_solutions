class Solution:
    def isValid(self, s: str) -> bool:
        brothers = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        
        array = []
        
        for c in s:
            if c in brothers:
                top_element = array.pop() if array else '#'
                if brothers[c] != top_element:
                    return False
            else:
                array.append(c)
                
        return len(array) == 0