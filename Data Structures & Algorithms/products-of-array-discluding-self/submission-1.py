class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outputs=[]
        for i in range(len(nums)):
            temp*=nums[i]
        for i in range(nums):
            outputs[i]=temp//nums[i]
        return outputs
