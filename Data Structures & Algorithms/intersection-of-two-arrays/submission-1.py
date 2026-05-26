class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lookupset = set(nums1)
        result = []
        for n in nums2:
            if n in lookupset:
                result.append(n)
                lookupset.remove(n)
        return result



        