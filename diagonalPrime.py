from typing import List

class Solution:
    # 2614. 对角线上的质数
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def is_prime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if (n % 2 == 0 or n % 3 == 0):
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i+2) == 0:
                    return False
                i += 6
            return True
        
        ans = 0
        ans = 0
        n = len(nums)
        
        n = len(nums)
        for i in range(n):
            x1 = nums[i][i]
            x2 = nums[i][n-i-1]
            if x1 > ans and is_prime(x1):
                ans = x1
            if x2 > ans and is_prime(x2):
                ans = x2
        return ans
            
            