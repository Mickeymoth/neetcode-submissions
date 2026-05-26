class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        lookup_set = set()
        for c in range(1,len(nums)+1):
            lookup_set.add(c)

        for c in nums:
            if c in lookup_set:
                lookup_set.remove(c)
        return  list(lookup_set)


        