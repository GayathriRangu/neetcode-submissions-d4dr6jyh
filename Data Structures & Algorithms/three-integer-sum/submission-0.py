class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        left=0
        right=len(nums)-1
        mid=int(right//2)
        #left+mid+right=0 left+mid=-right 1+2=-3
        while left<mid<right:
            if nums[left]+nums[mid]==-(nums[right]):
                return [nums[left],nums[mid],nums[right]]
            elif nums[left]+nums[mid]<-(nums[right]):
                left+=1
            elif nums[left]+nums[mid]>-(nums[right]):
                mid+=1
        return []
