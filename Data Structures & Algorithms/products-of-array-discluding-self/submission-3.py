class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outputs=[]
        temp=1
        for i in range(0,len(nums)):
            temp*=nums[i]
        for i in range(nums):
            outputs[i]=temp//nums[i]
        return outputs
