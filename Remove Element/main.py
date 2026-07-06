from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        index = 0
        for read in range(len(nums)):
            if nums[read] != val:
                nums[index] = nums[read]
                index += 1
        return index