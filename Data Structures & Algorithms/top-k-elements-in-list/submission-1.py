class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numdict={}
        for num in nums:
            if num not in numdict:
                numdict[num]=1
            numdict[num]+=1

        pairs=list(numdict.items())
        pairs.sort(key=lambda x:x[1], reverse=True)
        result=[]
        for i in range(k):
            number=pairs[i][0]
            result.append(number)

        # sorted_items=sorted(numdict.items(),key=lambda x:x[1],reverse=True)
        # result=[item[0] for item in sorted_items[:k]]
        return result