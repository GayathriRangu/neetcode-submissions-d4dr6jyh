class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newdict={}
        for i in range(len(nums)):
            key=nums[i]
            val=i
            newdict[key]=val
        for (i,j) in newdict.items():
            comkey=target-i
            newindex=newdict[comkey]
            if comkey in newdict and j!=newindex:
                return [j, newindex] 
        

        