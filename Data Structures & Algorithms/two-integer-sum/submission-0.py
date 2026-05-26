class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        PreviousMap = {}
        for i, n in  enumerate(nums):
            diff = target - n
            if diff in PreviousMap:
                return [PreviousMap[diff],i]
            PreviousMap[n] = i
            
            