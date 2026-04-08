class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #brute force wat: sort them off and groupt them if they are exactly the same
        sortedanagram={}
        sortedlists=[sorted(s) for s in strs]
        
        for i,j in zip(strs, sortedlists):
            if j not in sortedanagram:
                sortedanagram[j]=[]
            sortedanagram.append(i)
        return sortedanagram
        


        