class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outputs=[0]*len(nums)
        temp=1
        for i in range(0,len(nums)):
            temp*=nums[i]
        for i in range(len(nums)):
            if nums[i]!=0:
                outputs[i]=temp//nums[i]
            else:
                outputs[i]=temp
        return outputs
