class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''
        for i in s:
            if i.isalnum():
                new_s += i
        new_s = new_s.lower()
        # print(new_s)
        
        def check(left,right):
            #base case
            if left >= right:
                return True
            #charecters donot match
            if new_s[left] != new_s[right]:
                return False
            #recursive call
            return check(left+1, right-1)
        return check(0,len(new_s)-1)
            




        