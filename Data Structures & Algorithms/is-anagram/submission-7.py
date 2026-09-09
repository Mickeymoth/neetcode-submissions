class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt = {}

        if len(s)!= len(t):
            return False

        for i in range(len(s)):
            cnt[s[i]] = cnt.get(s[i],0) + 1
            cnt[t[i]] = cnt.get(t[i],0) - 1

        for val in cnt.values():
            if val != 0:
                return False
        return True


        
            
        
        