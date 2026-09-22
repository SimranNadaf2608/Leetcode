class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split(' ')
        if len(pattern) != len(word):
            return False
        h = {}
        h1 = {}
        ch = 0
        for ch , word in zip(pattern , word):
            print(ch , word)
            if ch in h:
                if h[ch] != word:
                    return False
            elif word in h1:
                if h1[word] != ch:
                    return False
            else:
                h[ch] = word
                h1[word] = ch
        return True