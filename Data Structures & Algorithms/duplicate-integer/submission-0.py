class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in nums:
            if i in nums and i!=j:
                return True
        return False        