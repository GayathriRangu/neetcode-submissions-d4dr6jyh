class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newdict={}
        for i in range(len(nums)):
            newdict[nums[i]]=i
        for (i,j) in newdict.items():
            if (target-i) in newdict:
                return [j, newdict[target-i]]
        

        