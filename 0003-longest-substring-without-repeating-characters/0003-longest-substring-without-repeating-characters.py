class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ''
        for i in range(len(s)):
            sub = ''
            for j in range(i, len(s)):
                if s[j] in sub:
                    break

                sub = sub+s[j]

                if len(sub)> len(longest):
                    longest = sub
        return len(longest)
                