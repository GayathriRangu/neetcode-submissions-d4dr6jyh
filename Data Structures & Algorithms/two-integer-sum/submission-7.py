class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # newdict={} #donoit build the entire dictionary at first
        # for i in range(len(nums)):
        #     key=nums[i]
        #     val=i
        #     newdict[key]=val
        seen={}
        for i, num in enumerate(nums):
            complement= target-num
            if complement in seen:
                return [seen[complement],i]
            seen[num]=i 
        

        