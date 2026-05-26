class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        isDuplicate = set()

        for n in nums:
            if n not in isDuplicate:
              isDuplicate.add(n)
            else:
                return True
        return False  

            


    
        