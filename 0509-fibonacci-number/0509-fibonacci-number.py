class Solution:
    def fib(self, n: int) -> int:
        def fibb(n):
            if n <= 1:
                return n
            last = fibb(n-1)
            slast = fibb(n-2)
            return last+slast
        return fibb(n)
        