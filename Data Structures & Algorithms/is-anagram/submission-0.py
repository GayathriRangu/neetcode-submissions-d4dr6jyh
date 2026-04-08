class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s={}
        hash_t={}
        for i in s:
            if i in hash_s:
                hash_s[i]+=1 #increase the count
            else:
                hash_s[i]=1
        for i in t:
            if i in hash_t:
                hash_t[i]+=1
            else:
                hash_t[i]=1
        for i,j in hash_s.items():
            if i in hash_t and j==has_t[i]:
                pass
            else:
                return False
        return True

        