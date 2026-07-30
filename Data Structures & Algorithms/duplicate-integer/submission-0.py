class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        pointer = set(nums)
        
        if len(pointer) ==len(nums):
            return False
        else:
            return True