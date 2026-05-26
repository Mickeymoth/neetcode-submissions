class Solution:
    def isHappy(self, n: int) -> bool:
        lookup = set()

        while n not in lookup:
            lookup.add(n)
            n = self.sum_of_squares_digit(n)
            if n == 1:
                return True 
        return False
        
        
    def sum_of_squares_digit(self, n:int)->int:
        output = 0

        while n>0:
            digit = n%10
            digit = digit**2
            output+=digit
            n = n//10
        return output 
