class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        j = 0
        for i in t:
            if i == s[j]:
                j += 1
            if j == len(s):
                return True
        return False        


        # if len(s) == 0:
        #     return True

        # j = 0
        # for i in t:
        #     if i == s[j]:
        #         j += 1
        #     if j == len(s):
        #         return True
        # return False            
        