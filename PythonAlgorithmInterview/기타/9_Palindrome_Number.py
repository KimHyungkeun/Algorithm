class Solution:
    def isPalindrome(self, x: int) -> bool:
        nums = str(x)
        return nums[:] == nums[::-1]