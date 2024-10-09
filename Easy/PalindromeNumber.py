class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        rev = 0
        temp = x
        while temp:
            rev = rev*10 + temp%10
            temp //= 10
        if x == rev:
            return True
        else:
            return False

x=532
obj=Solution()
print(obj.isPalindrome(x))
