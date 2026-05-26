class Solution:
    def firstUniqChar(self, s: str) -> int:
        countS = {}
        for i in range(len(s)):
            countS[s[i]] = 1+countS.get(s[i],0)
        for i,c in enumerate(s):
            if countS[c]==1:
                return i
        return -1





        