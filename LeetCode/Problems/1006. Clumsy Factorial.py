class Solution:
    def clumsy(self, n: int) -> int:
        if n < 6 or n == 6:
            if n == 6:
                return 8 
            elif n == 5:
                return 7
            elif n == 4:
                return 7
            elif n == 3:
                return 6
            elif n == 2:
                return 2
            elif n == 1:
                return 1
            else:
                return 0
        else:
            return n*(n-1)//(n-2)+(n-3)-2*((n-4)*(n-5)//(n-6))+Solution().clumsy(n-4)
