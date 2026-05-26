class Solution:
    def firstUniqChar(self, s: str) -> int:
        CountS = {}
        for i in range(len(s)):
            CountS[s[i]] = 1 + CountS.get(s[i],0)
        for i,c in enumerate(s):
            if CountS[c]==1:
                return i
        return -1



        