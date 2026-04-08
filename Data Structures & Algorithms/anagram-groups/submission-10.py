class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #brute force wat: character frequency arrays for each anagram and compare them

        groups=[]
        processed=[False]*len(strs)

        for i in range(len(strs)):
            if processed[i]:
                continue
            current_group=[strs[i]]
            processed[i]=True

            count_i=[0]*26
            for char in strs[i]:
                count_i[ord(char)-ord('a')]+=1
            for j in range(i+1,len(strs)):
                if processed[j]:
                    continue
                count_j=[0]*26
                for char in strs[j]:
                    count_j[ord(char)-ord('a')]+=1
                if count_i==count_j:
                    current_group.append(strs[j])
                    processed[j]=True
            groups.append(current_group)

        return groups