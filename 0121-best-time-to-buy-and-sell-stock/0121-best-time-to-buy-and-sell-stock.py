class Solution:
    def maxProfit(self, p: list[int]) -> int:
        minn = [0] * len(p)
        minn[0] = p[0] 
        maxx = 0

        for i in range(1, len(p)):
            minn[i] = min(p[i], minn[i-1])
        print(minn)

        for i in range(1,len(p)):
            maxx = max(maxx, (p[i]-minn[i-1]))
        return maxx
        