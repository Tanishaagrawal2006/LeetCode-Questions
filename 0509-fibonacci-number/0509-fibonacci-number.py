class Solution(object):
    def fib(self, n):
        
        #base case
        if n == 0 or n == 1:
            return n
        
        #recursive case
        else:
            return self.fib(n-1) + self.fib(n-2)
        