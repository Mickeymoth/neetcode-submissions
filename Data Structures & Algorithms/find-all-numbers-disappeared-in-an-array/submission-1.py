class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        for n in range(1,n+1):
            if n not in nums:
                result.append(n)
        return result

        