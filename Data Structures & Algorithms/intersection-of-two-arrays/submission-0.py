class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        EmptySet = set(nums1)
        result = []

        for n in nums2:
            if n in EmptySet:
                result.append(n)
                EmptySet.remove(n)
        return result

        


        