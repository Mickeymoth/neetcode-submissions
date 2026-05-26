class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        CountS = {}
        result = 0
        MaxCount = 0
        for n in nums:
            CountS[n] = 1+CountS.get(n,0)
            if CountS[n]>MaxCount:
                result = n
                MaxCount = CountS[n]
        return result

    
        