class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        EmptySet = set()
        for n in nums :
            if n in EmptySet:
                return True
            EmptySet.add(n)
        return False
            