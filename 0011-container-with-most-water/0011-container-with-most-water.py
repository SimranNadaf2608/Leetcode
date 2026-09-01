class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxx = 0
        minn = 0
        left = 0
        right = len(height)-1
        while left < right:
            width = right - left
            minn = min(height[left], height[right])
            area = width*minn
            maxx = max(area, maxx)
            if height[left] == height[right]:
                right -= 1
            elif height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxx
        