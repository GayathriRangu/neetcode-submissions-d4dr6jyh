class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s={}
        hash_t={}
        if s.len() == t.len():
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
                if i in hash_t and j==hash_t[i]:
                    pass #how do u check if both dictonaryies are the same???
                else:
                    return False
            return True
        else:
            return False
            