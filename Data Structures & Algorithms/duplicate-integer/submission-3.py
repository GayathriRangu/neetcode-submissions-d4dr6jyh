class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen={}
        for i,j in enumerate(nums):
            if j in seen:
                return True
            else:
                seen[i]=j
        return False 