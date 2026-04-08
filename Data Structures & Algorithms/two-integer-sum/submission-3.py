class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newdict={}
        for i in range(len(nums)):
            key=nums[i]
            val=i
            newdict[key]=val
        for (i,j) in newdict.items():
            if (target-i) in newdict and i!=j:
                return [j, newdict[target-i]] 
        

        