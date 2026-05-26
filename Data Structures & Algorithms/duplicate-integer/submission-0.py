class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        empty_set = set()
        for n in nums:
            if n in empty_set:
                return True
            empty_set.add(n)
        return False