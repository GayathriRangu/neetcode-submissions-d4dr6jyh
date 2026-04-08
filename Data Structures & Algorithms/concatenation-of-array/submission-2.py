class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        ans=nums.extend(nums)
        return ans
        