class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxii = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                maxii = max(count, maxii)
            else:
                count = 0
        return maxii        
            
        