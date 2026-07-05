from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        smallest = min(strs)
        biggest = max(strs)
        pre = []
        for i in range (len(smallest)):
            if i < len(biggest) and smallest[i] == biggest[i]:
                pre.append(smallest[i])
            else:
                break
        return "".join(pre)